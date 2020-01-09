from PyQt5.QtCore import QThread, pyqtSignal
import time

class TimeCounter(QThread):
    signalMove = pyqtSignal(bool)

    def __init__(self, sleepTime = 10., parent=None):
        super(TimeCounter, self).__init__(parent)
        self.sleepTime = sleepTime
        self.startThread = False

    def run(self) -> None:
        while(True):
            time.sleep(self.sleepTime)
            self.signalMove.emit(True)
            if ~self.startThread:
             break

    def timeStart(self):
        self.startThread = True
    def timeStop(self):
        self.startThread = False