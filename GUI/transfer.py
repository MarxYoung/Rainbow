# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transfer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import os


class Ui_Form(object):
    def setupUi(self, Form):
        self.form = Form
        Form.setObjectName("Form")
        Form.resize(1183, 688)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(820, 160, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(320, 160, 251, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 160, 67, 20))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 160, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_2.clicked.connect(lambda: self.on_pushButton_2_clicked())
        self.lineEdit.text()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "send"))
        self.label.setText(_translate("Form", "sendto:"))
        self.pushButton_2.setText(_translate("Form", "Select"))

    def on_pushButton_2_clicked(self):
        files, _ = QFileDialog.getOpenFileNames(self.form, "open file", os.getcwd())

        if len(files) == 0:
            print("\n取消选择")
            return

        print(files)

