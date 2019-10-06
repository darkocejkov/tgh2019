# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ViewCoverageGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainViewCoverage(object):
    def setupUi(self, mainViewCoverage):
        mainViewCoverage.setObjectName("mainViewCoverage")
        mainViewCoverage.resize(800, 600)
        mainViewCoverage.setStyleSheet("background-color:rgb(49, 99, 170)")
        self.centralwidget = QtWidgets.QWidget(mainViewCoverage)
        self.centralwidget.setObjectName("centralwidget")
        self.lsPolicyInfo = QtWidgets.QListView(self.centralwidget)
        self.lsPolicyInfo.setGeometry(QtCore.QRect(30, 100, 741, 211))
        self.lsPolicyInfo.setStyleSheet("background-color:#FFFFFF")
        self.lsPolicyInfo.setObjectName("lsPolicyInfo")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(290, 30, 241, 51))
        self.lblTitle.setObjectName("lblTitle")
        self.lblForgotInfo = QtWidgets.QLabel(self.centralwidget)
        self.lblForgotInfo.setGeometry(QtCore.QRect(150, 330, 491, 111))
        self.lblForgotInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblForgotInfo.setWordWrap(True)
        self.lblForgotInfo.setObjectName("lblForgotInfo")
        self.btnManulife = QtWidgets.QPushButton(self.centralwidget)
        self.btnManulife.setGeometry(QtCore.QRect(120, 460, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btnManulife.setFont(font)
        self.btnManulife.setStyleSheet("")
        self.btnManulife.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("manulife.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnManulife.setIcon(icon)
        self.btnManulife.setIconSize(QtCore.QSize(120, 120))
        self.btnManulife.setObjectName("btnManulife")
        self.btnIntact = QtWidgets.QPushButton(self.centralwidget)
        self.btnIntact.setGeometry(QtCore.QRect(270, 460, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btnIntact.setFont(font)
        self.btnIntact.setStyleSheet("")
        self.btnIntact.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("intact.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnIntact.setIcon(icon1)
        self.btnIntact.setIconSize(QtCore.QSize(120, 120))
        self.btnIntact.setObjectName("btnIntact")
        self.btnCooperators = QtWidgets.QPushButton(self.centralwidget)
        self.btnCooperators.setGeometry(QtCore.QRect(420, 460, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btnCooperators.setFont(font)
        self.btnCooperators.setStyleSheet("")
        self.btnCooperators.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("cooperators.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCooperators.setIcon(icon2)
        self.btnCooperators.setIconSize(QtCore.QSize(120, 120))
        self.btnCooperators.setObjectName("btnCooperators")
        self.btnDesjardins = QtWidgets.QPushButton(self.centralwidget)
        self.btnDesjardins.setGeometry(QtCore.QRect(560, 460, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btnDesjardins.setFont(font)
        self.btnDesjardins.setStyleSheet("background-color:#FFFFFF")
        self.btnDesjardins.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("desjardins.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDesjardins.setIcon(icon3)
        self.btnDesjardins.setIconSize(QtCore.QSize(120, 120))
        self.btnDesjardins.setObjectName("btnDesjardins")
        mainViewCoverage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainViewCoverage)
        self.statusbar.setObjectName("statusbar")
        mainViewCoverage.setStatusBar(self.statusbar)

        self.retranslateUi(mainViewCoverage)
        QtCore.QMetaObject.connectSlotsByName(mainViewCoverage)

    def retranslateUi(self, mainViewCoverage):
        _translate = QtCore.QCoreApplication.translate
        mainViewCoverage.setWindowTitle(_translate("mainViewCoverage", "View Coverage"))
        self.lblTitle.setText(_translate("mainViewCoverage", "<html><head/><body><p><span style=\" font-size:26pt; color:#ffffff;\">Your Coverage</span></p></body></html>"))
        self.lblForgotInfo.setText(_translate("mainViewCoverage", "<html><head/><body><p><span style=\" font-size:26pt; color:#ffffff;\">Forgot your policy information? Check Here!</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainViewCoverage = QtWidgets.QMainWindow()
    ui = Ui_mainViewCoverage()
    ui.setupUi(mainViewCoverage)
    mainViewCoverage.show()
    sys.exit(app.exec_())
