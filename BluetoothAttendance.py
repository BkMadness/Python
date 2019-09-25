# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BluetoothAttendance.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import bluetooth 
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(788, 660)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 255);"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 270, 91, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.studentno = QtGui.QLineEdit(Dialog)
        self.studentno.setGeometry(QtCore.QRect(120, 260, 101, 27))
        self.studentno.setObjectName(_fromUtf8("studentno"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 220, 91, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.macaddress = QtGui.QLineEdit(Dialog)
        self.macaddress.setGeometry(QtCore.QRect(120, 220, 201, 27))
        self.macaddress.setObjectName(_fromUtf8("macaddress"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 310, 81, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.name = QtGui.QLineEdit(Dialog)
        self.name.setGeometry(QtCore.QRect(120, 300, 201, 27))
        self.name.setObjectName(_fromUtf8("name"))
        self.moduleid = QtGui.QLineEdit(Dialog)
        self.moduleid.setGeometry(QtCore.QRect(550, 220, 113, 27))
        self.moduleid.setObjectName(_fromUtf8("moduleid"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 360, 81, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lastname = QtGui.QLineEdit(Dialog)
        self.lastname.setGeometry(QtCore.QRect(120, 350, 201, 27))
        self.lastname.setObjectName(_fromUtf8("lastname"))
        self.dob = QtGui.QLineEdit(Dialog)
        self.dob.setGeometry(QtCore.QRect(120, 410, 113, 27))
        self.dob.setObjectName(_fromUtf8("dob"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 420, 68, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(440, 230, 71, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(440, 270, 68, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.tittle = QtGui.QLineEdit(Dialog)
        self.tittle.setGeometry(QtCore.QRect(550, 260, 201, 27))
        self.tittle.setObjectName(_fromUtf8("tittle"))
        self.startime = QtGui.QLineEdit(Dialog)
        self.startime.setGeometry(QtCore.QRect(550, 300, 201, 27))
        self.startime.setObjectName(_fromUtf8("startime"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(440, 310, 81, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(30, 470, 68, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.male = QtGui.QRadioButton(Dialog)
        self.male.setGeometry(QtCore.QRect(130, 470, 117, 22))
        self.male.setObjectName(_fromUtf8("male"))
        self.female = QtGui.QRadioButton(Dialog)
        self.female.setGeometry(QtCore.QRect(200, 470, 117, 22))
        self.female.setObjectName(_fromUtf8("female"))
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(440, 350, 68, 17))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.endtime = QtGui.QLineEdit(Dialog)
        self.endtime.setGeometry(QtCore.QRect(550, 340, 201, 27))
        self.endtime.setObjectName(_fromUtf8("endtime"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 180, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 570, 99, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.submit = QtGui.QPushButton(Dialog)
        self.submit.setGeometry(QtCore.QRect(500, 570, 99, 27))
        self.submit.setObjectName(_fromUtf8("submit"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(280, 20, 181, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(490, 20, 68, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(30, 10, 151, 151))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
       
   
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Bluetooth Attendance Register", None))
        self.label.setText(_translate("Dialog", "Student No", None))
        self.label_2.setText(_translate("Dialog", "Mac Address", None))
        self.label_3.setText(_translate("Dialog", "First Name", None))
        self.label_4.setText(_translate("Dialog", "Last Name", None))
        self.label_5.setText(_translate("Dialog", "DOB", None))
        self.label_6.setText(_translate("Dialog", "Module ID", None))
        self.label_7.setText(_translate("Dialog", "Tittle", None))
        self.label_8.setText(_translate("Dialog", "Start-Time", None))
        self.label_13.setText(_translate("Dialog", "Sex", None))
        self.male.setText(_translate("Dialog", "Male", None))
        self.female.setText(_translate("Dialog", "Female", None))
        self.label_14.setText(_translate("Dialog", "End-Time", None))
        self.pushButton.setText(_translate("Dialog", "Scan", None))
        self.pushButton_2.setText(_translate("Dialog", "Clear", None))
        self.submit.setText(_translate("Dialog", "Submit", None))
        self.label_9.setText(_translate("Dialog", "Number of Devices Found ", None))
        self.label_10.setText(_translate("Dialog", "0", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())