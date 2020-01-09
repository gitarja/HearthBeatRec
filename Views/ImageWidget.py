# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimediaWidgets

class Ui_ImageWidget(object):

    def setupUi(self, ImageWidget):
        ImageWidget.setObjectName("ImageWidget")
        ImageWidget.resize(1024, 768)
        ImageWidget.setAutoFillBackground(False)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.horizontalLayoutWidget = QtWidgets.QWidget(ImageWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imageLabel = QtWidgets.QLabel()
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.horizontalLayout.addWidget(self.imageLabel)


        self.retranslateUi(ImageWidget)
        QtCore.QMetaObject.connectSlotsByName(ImageWidget)

    def retranslateUi(self, ImageWidget):
        _translate = QtCore.QCoreApplication.translate
        ImageWidget.setWindowTitle(_translate("ImageWidget", "Form"))

    def handleError(self):
        print("Error" + self.mediaPlayer.errorString())


