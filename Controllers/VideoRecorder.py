import cv2
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import  QMessageBox
class VideoRecorder(QThread):

    def __init__(self, path=None):
        QThread.__init__(self)
        self.path = path
        try:
            self.cap = cv2.VideoCapture(0)
        except:
            QMessageBox.warning(self.view, "Error", "ウェブカムが見つかりません")



    def setFileName(self, path):

        self.record = True
        self.path = path

    def run(self) -> None:
        # video recorder

        w = 640
        h = 480
        fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
        out = cv2.VideoWriter(self.path, fourcc, 30.0, (int(w), int(h)))
        # record video
        while (self.record & self.cap.isOpened()):
            ret, frame = self.cap.read()
            if ret:
                resizedFrame = cv2.resize(frame, (w, h))
                out.write(resizedFrame)
                # cv2.imshow('Video Stream', frame)

            else:
                break
        out.release()
        self.cap.release()


    def stop(self):
        self.record = False
        cv2.destroyAllWindows()
