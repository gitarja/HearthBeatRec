# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWidget(object):

    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(459, 264)
        self.frame = QtWidgets.QFrame(MainWidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 431, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 90, 421, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.nameField = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.nameField.setObjectName("nameField")
        self.gridLayout.addWidget(self.nameField, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.sexField = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.sexField.setObjectName("sexField")
        self.sexField.addItem("")
        self.sexField.addItem("")
        self.gridLayout.addWidget(self.sexField, 0, 3, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 180, 421, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout.addWidget(self.startButton)
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 421, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.personalLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.personalLabel.setFont(font)
        self.personalLabel.setObjectName("personalLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.personalLabel)
        self.dirLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dirLabel.setFont(font)
        self.dirLabel.setObjectName("dirLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.dirLabel)
        self.dirButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.dirButton.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dirButton.setFont(font)
        self.dirButton.setObjectName("dirButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dirButton)
        self.personalBox = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.personalBox.setFont(font)
        self.personalBox.setObjectName("personalBox")
        self.personalBox.addItem("")
        self.personalBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.personalBox)
        self.dirField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.dirField.setEnabled(False)
        self.dirField.setObjectName("dirField")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dirField)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 80, 421, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(MainWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "Form"))
        self.label_2.setText(_translate("MainWidget", "性別"))
        self.label.setText(_translate("MainWidget", "名前"))
        self.sexField.setItemText(0, _translate("MainWidget", "M"))
        self.sexField.setItemText(1, _translate("MainWidget", "F"))
        self.startButton.setText(_translate("MainWidget", "始める"))
        self.personalLabel.setText(_translate("MainWidget", "個人的な写真"))
        self.dirLabel.setText(_translate("MainWidget", "写真ディレクトリ"))
        self.dirButton.setText(_translate("MainWidget", "開く"))
        self.personalBox.setItemText(0, _translate("MainWidget", "なし"))
        self.personalBox.setItemText(1, _translate("MainWidget", "あり"))

    def fileName(self):
        return  "_"+self.nameField.text()+"_"+self.sexField.currentText()

    def pictureDict(self):
        file = str(QFileDialog.getExistingDirectory(None, "Select Directory",  QtCore.QDir.rootPath()))

        return file


