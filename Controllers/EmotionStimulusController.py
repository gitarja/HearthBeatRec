from PyQt5.QtWidgets import QApplication, QDialog, QDesktopWidget, QMessageBox
from PyQt5 import QtCore
import sys
from Views.MainWindow import Ui_MainWindow
from Views.ImageWidget import Ui_ImageWidget
from Views.QuestionWidget import Ui_QuestionWidget
from Views.MainWidget import Ui_MainWidget
from Conf.Setting import Setting
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from Controllers.ImageGenerator import ImageGenerator
from Controllers.TimeCounter import TimeCounter
from Controllers.VideoRecorder import VideoRecorder
import os, psutil
import pandas as pd
from datetime import datetime


class EmotionStimulusController:
    def __init__(self):
        # print(sys.getrecursionlimit())
        self.app = QApplication(sys.argv)
        self.setting = Setting("Conf\\Setting.yaml")

        self.view = Ui_MainWindow()
        mainWidget = Ui_MainWidget()

        mainWidget.setupUi(self.view.widget)
        # Set widget to center
        self.moveToCenter()
        mainWidget.startButton.clicked.connect(self.startTest(mainWidget))
        mainWidget.personalBox.activated.connect(self.activateDirectory(mainWidget))
        mainWidget.dirButton.clicked.connect(self.selectPicturesDict(mainWidget))

        self.mainWidget = mainWidget
        # numimages and sleeptime
        self.numImages = 130
        self.sleepTime = 10

        # imageThread
        self.imageGen = ImageGenerator(self.setting.conf["IMAGEDAT_DIR"])

        # time counter
        self.timeCounter = TimeCounter(self.sleepTime)
        self.timeCounter.signalMove.connect(self.showQuestion)

        # time start
        self.times = [0, 0]
        self.timesTest = [0, 0]

        # index
        self.index = 0
        # data
        self.data = pd.DataFrame(
            columns=["Time_Start", "Time_End", "TestTime_Start", "TestTime_End", "Valence", "Arousal", "Emotion",
                     "Image", "Valence_label", "Arousal_label"])
        # filename for experiment data
        self.filename = str(datetime.now()).replace(" ", "_").replace(":", "-")
        self.subjectname = ""

        # video recorder
        self.videoRecorder = VideoRecorder()

        # personal picture
        self.personal = False
        self.personalDict = ""

    def activateDirectory(self, widget):
        def activate():
            idx = widget.personalBox.currentIndex()
            if idx == 1:
                widget.dirButton.setEnabled(True)
                self.personal = True
            else:
                widget.dirButton.setEnabled(False)
                widget.dirField.setText("")
                self.personal = False

        return activate

    def selectPicturesDict(self, widget):
        def select():
            fileDir = widget.pictureDict()
            widget.dirField.setText(fileDir)
            self.personalDict = fileDir

        return select

    def startTest(self, widget):
        def start():
            if (widget.nameField.text() == ""):
                QMessageBox.information(self.view, "Information", "Please insert your name")
                return
            self.subjectname = widget.fileName()
            self.filename += self.subjectname + "_" + str(self.personal) + ".csv"
            # start video recording
            videoname = str(datetime.now()).replace(" ", "_").replace(":", "-") + self.subjectname + ".avi"
            self.videoRecorder.setFileName(os.path.join(self.setting.conf["VIDEO_DIR"], videoname))
            self.videoRecorder.start()
            self.imageGen.setParams(widget.sexField.currentText())
            if self.personal:
                imgLen = self.imageGen.readPersonalPictures(self.personalDict)
                if imgLen < self.setting.conf["MIN_PERSONAL_IMAGES"]:
                    QMessageBox.warning(self.view, "Error", str(self.setting.conf["MIN_PERSONAL_IMAGES"])+"枚の写真は必要です。")
                    return

            self.showImage()

        return start

    def moveToCenter(self):
        self.view.widget.move(
            self.app.desktop().screen().rect().center() - self.view.widget.rect().center())

    def showImage(self):
        try:
            # set bg color
            self.view.setStyleSheet("background-color: black;")
            # clear the widget
            self.view.widget.hide()
            self.view.widget.children()[0].setParent(None)
            # set the widget
            widget = Ui_ImageWidget()
            widget.setupUi(self.view.widget)
            self.view.widget.activateWindow()

            self.setImage(widget.imageLabel)
            # move to center
            self.moveToCenter()
            # show the widget
            self.view.widget.update()
            self.view.widget.show()
            self.times[0] = datetime.now()




        except:
            raise ("Error when trying to show image")

    def showQuestion(self):
        # set bg color
        self.view.setStyleSheet("")
        # record the start time
        self.timesTest[0] = datetime.now()
        # terminate video recording

        self.times[1] = datetime.now()
        # terminate counter
        self.timeCounter.timeStop()
        # clear the widget
        self.view.widget.hide()
        self.view.widget.children()[0].setParent(None)
        # set the widget
        widget = Ui_QuestionWidget()
        widget.setupUi(self.view.widget)
        widget.setValenceArousal(self.setting.conf["VALENCE_AROUSAL"])
        widget.nextButton.clicked.connect(self.getAnswer(widget))
        # move to center
        self.moveToCenter()
        # show the widget
        self.view.widget.update()
        self.view.widget.show()

    def getAnswer(self, widget):
        def get():
            self.timesTest[1] = datetime.now()
            valenceLevel = widget.valenceLevel()
            arousalLevel = widget.arousalLevel()
            emotionLevel = widget.emotionLevel()
            timeStart = self.times[0]
            timeEnd = self.times[1]
            testTimeStart = self.timesTest[0]
            testTimeEnd = self.timesTest[1]
            self.data = self.data.append({"Time_Start": timeStart, "Time_End": timeEnd, "TestTime_Start": testTimeStart,
                                          "TestTime_End": testTimeEnd, "Valence": valenceLevel, "Arousal": arousalLevel,
                                          "Emotion": emotionLevel, "Image": self.image, "Valence_label":self.valLabel, "Arousal_label":self.arLabel}, ignore_index=True)
            self.index += 1
            if (self.index >= self.numImages):
                self.showProcessDialog(os.path.join(self.setting.conf["RESULT_DIR"], self.filename),
                                       os.path.join(self.setting.conf["RESULT_DIR"], "imgList_" + self.filename))
            else:
                self.saveFile(os.path.join(self.setting.conf["RESULT_DIR"], self.filename),
                              os.path.join(self.setting.conf["RESULT_DIR"], "imgList_" + self.filename))
                self.showImage()

        return get

    def setImage(self, imageLabel):

        if self.personal:
            img, val, ar, personalImage, gif = self.imageGen.pickImagePersonal()
            if personalImage:
                path = os.path.join(self.personalDict, img)
            else:
                path = os.path.join(self.setting.conf["OASIS_DIR"], img)
        else:
            img, val, ar, gif = self.imageGen.pickImage()
            path = os.path.join(self.setting.conf["OASIS_DIR"], img)
        self.image = img
        self.valLabel = val
        self.arLabel = ar

        # print(os.path.join(self.setting.conf["OASIS_DIR"], path))
        imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        if gif==1:
            movie = QMovie(path, QtCore.QByteArray())
            movie.setScaledSize(QtCore.QSize().scaled(1024, 768, QtCore.Qt.KeepAspectRatio))
            imageLabel.setMovie(movie)
            movie.start()
        else:
            pixmap = QPixmap(path)
            resizedPix = pixmap.scaled(1024, 768, QtCore.Qt.KeepAspectRatio)
            imageLabel.setPixmap(resizedPix)
            imageLabel.update()
        self.timeCounter.start()

    def showProcessDialog(self, resultPath, imageListPath):
        try:
            QMessageBox.information(self.view, "Information", "Test is finished")
            self.saveFile(resultPath, imageListPath)
            self.videoRecorder.stop()
            self.quit()

        except:
            QMessageBox.warning(self.view, "Error", "Cannot save file")

    def saveFile(self, resultPath, imageListPath):
        self.data.to_csv(resultPath)
        imageList = pd.DataFrame({"imageList": self.imageGen.imageList})
        imageList.to_csv(imageListPath)

    def quit(self):
        self.videoRecorder.terminate()
        self.timeCounter.terminate()
        self.app.closeAllWindows()
        self.killProcess()
        self.app.exit()

    def killProcess(self):
        pid = os.getpid()
        parent = psutil.Process(pid)
        for child in parent.children(recursive=True):
            child.kill()
            parent.kill()

    def run(self):
        self.view.showFullScreen()
        return self.app.exec_()
