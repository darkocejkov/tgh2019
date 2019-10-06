# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddPolicyGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainAddPolicy(object):
    def setupUi(self, mainAddPolicy):
        mainAddPolicy.setObjectName("mainAddPolicy")
        mainAddPolicy.resize(800, 600)
        mainAddPolicy.setAutoFillBackground(False)
        mainAddPolicy.setStyleSheet("background-color:rgb(49, 99, 170)")
        self.centralwidget = QtWidgets.QWidget(mainAddPolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 60, 141, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 251, 61))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 170, 71, 61))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 220, 161, 61))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 280, 161, 61))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 340, 221, 61))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 400, 101, 61))
        self.label_7.setObjectName("label_7")
        self.leSponsor = QtWidgets.QLineEdit(self.centralwidget)
        self.leSponsor.setGeometry(QtCore.QRect(290, 80, 411, 21))
        self.leSponsor.setAutoFillBackground(False)
        self.leSponsor.setStyleSheet("background-color:#FFFFFF;")
        self.leSponsor.setObjectName("leSponsor")
        self.lePolicy = QtWidgets.QLineEdit(self.centralwidget)
        self.lePolicy.setGeometry(QtCore.QRect(290, 140, 411, 21))
        self.lePolicy.setStyleSheet("background-color:#FFFFFF;")
        self.lePolicy.setObjectName("lePolicy")
        self.leID = QtWidgets.QLineEdit(self.centralwidget)
        self.leID.setGeometry(QtCore.QRect(290, 190, 411, 21))
        self.leID.setStyleSheet("background-color:#FFFFFF")
        self.leID.setObjectName("leID")
        self.leCompany = QtWidgets.QLineEdit(self.centralwidget)
        self.leCompany.setGeometry(QtCore.QRect(290, 250, 411, 21))
        self.leCompany.setAutoFillBackground(False)
        self.leCompany.setStyleSheet("background-color:#FFFFFF;")
        self.leCompany.setObjectName("leCompany")
        self.leBaseAmt = QtWidgets.QLineEdit(self.centralwidget)
        self.leBaseAmt.setGeometry(QtCore.QRect(290, 310, 411, 21))
        self.leBaseAmt.setStyleSheet("background-color:#FFFFFF;")
        self.leBaseAmt.setObjectName("leBaseAmt")
        self.leAdjustedAmt = QtWidgets.QLineEdit(self.centralwidget)
        self.leAdjustedAmt.setGeometry(QtCore.QRect(290, 360, 411, 21))
        self.leAdjustedAmt.setStyleSheet("background-color:#FFFFFF;")
        self.leAdjustedAmt.setObjectName("leAdjustedAmt")
        self.lblMainLogo = QtWidgets.QLabel(self.centralwidget)
        self.lblMainLogo.setGeometry(QtCore.QRect(650, 460, 141, 111))
        self.lblMainLogo.setText("")
        self.lblMainLogo.setPixmap(QtGui.QPixmap("ids-white.png"))
        self.lblMainLogo.setScaledContents(True)
        self.lblMainLogo.setObjectName("lblMainLogo")
        self.combobType = QtWidgets.QComboBox(self.centralwidget)
        self.combobType.setGeometry(QtCore.QRect(300, 420, 191, 22))
        self.combobType.setStyleSheet("background-color:#FFFFFF;")
        self.combobType.setObjectName("combobType")
        self.btnGoPolicy = QtWidgets.QPushButton(self.centralwidget)
        self.btnGoPolicy.setGeometry(QtCore.QRect(370, 510, 75, 23))
        self.btnGoPolicy.setStyleSheet("background-color:#FFFFFF;")
        self.btnGoPolicy.setObjectName("btnGoPolicy")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(330, 20, 161, 41))
        self.label_9.setObjectName("label_9")
        mainAddPolicy.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainAddPolicy)
        self.statusbar.setObjectName("statusbar")
        mainAddPolicy.setStatusBar(self.statusbar)

        self.retranslateUi(mainAddPolicy)
        QtCore.QMetaObject.connectSlotsByName(mainAddPolicy)

    def retranslateUi(self, mainAddPolicy):
        _translate = QtCore.QCoreApplication.translate
        mainAddPolicy.setWindowTitle(_translate("mainAddPolicy", "Add Policy"))
        self.label.setText(_translate("mainAddPolicy", "<html><head/><body><p><span style=\" font-size:26pt; color:#ffffff;\">Sponsor:</span></p></body></html>"))
        self.label_2.setText(_translate("mainAddPolicy", "<html><head/><body><p><span style=\" font-size:26pt; color:#ffffff;\">Policy/Group #:</span></p></body></html>"))
        self.label_3.setText(_translate("mainAddPolicy", "<html><head/><body><p><span style=\" font-size:26pt; color:#ffffff;\">ID#:</span></p></body></html>"))
        self.label_4.setText(_translate("mainAddPolicy", "<html><head/><body><p><span style=\" font-size:26pt; color:#ffffff;\">Company:</span></p></body></html>"))
        self.label_5.setText(_translate("mainAddPolicy", "<html><head/><body><p><span style=\" font-size:26pt; color:#ffffff;\">Base Amt:</span></p></body></html>"))
        self.label_6.setText(_translate("mainAddPolicy", "<html><head/><body><p><span style=\" font-size:26pt; color:#ffffff;\">Adjusted Amt:</span></p></body></html>"))
        self.label_7.setText(_translate("mainAddPolicy", "<html><head/><body><p><span style=\" font-size:26pt; color:#ffffff;\">Type:</span></p></body></html>"))
        self.btnGoPolicy.setText(_translate("mainAddPolicy", "GO"))
        self.label_9.setText(_translate("mainAddPolicy", "<html><head/><body><p><span style=\" font-size:26pt; text-decoration: underline; color:#ffffff;\">Add Policy</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainAddPolicy = QtWidgets.QMainWindow()
    ui = Ui_mainAddPolicy()
    ui.setupUi(mainAddPolicy)
    mainAddPolicy.show()
    sys.exit(app.exec_())
