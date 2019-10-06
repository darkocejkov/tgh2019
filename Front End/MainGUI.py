from PyQt5 import QtCore, QtGui, QtWidgets
from AddUserGUI import Ui_mainAddUser
from AddPolicyGUI import Ui_mainAddPolicy
from ViewCoverageGUI import Ui_mainViewCoverage

class Ui_MainWindow(object):
    def openAddUser(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_mainAddUser()
        self.ui.setupUi(self.window)
        self.window.show()
    def openAddPolicy(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_mainAddPolicy()
        self.ui.setupUi(self.window)
        self.window.show()
    def openViewCoverage(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_mainViewCoverage()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:rgb(49, 99, 170)")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblLogo = QtWidgets.QLabel(self.centralwidget)
        self.lblLogo.setGeometry(QtCore.QRect(30, 150, 331, 261))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.lblLogo.setFont(font)
        self.lblLogo.setText("")
        self.lblLogo.setPixmap(QtGui.QPixmap("ids-white.png"))
        self.lblLogo.setScaledContents(True)
        self.lblLogo.setObjectName("lblLogo")
        self.lblAddUser_img = QtWidgets.QLabel(self.centralwidget)
        self.lblAddUser_img.setGeometry(QtCore.QRect(410, 90, 81, 121))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.lblAddUser_img.setFont(font)
        self.lblAddUser_img.setText("")
        self.lblAddUser_img.setPixmap(QtGui.QPixmap("add-user-white.png"))
        self.lblAddUser_img.setScaledContents(True)
        self.lblAddUser_img.setObjectName("lblAddUser_img")
        self.lblAddPolicy_img = QtWidgets.QLabel(self.centralwidget)
        self.lblAddPolicy_img.setGeometry(QtCore.QRect(390, 270, 111, 121))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.lblAddPolicy_img.setFont(font)
        self.lblAddPolicy_img.setText("")
        self.lblAddPolicy_img.setPixmap(QtGui.QPixmap("add-policy-white.png"))
        self.lblAddPolicy_img.setScaledContents(True)
        self.lblAddPolicy_img.setObjectName("lblAddPolicy_img")
        self.lblViewCoverage_img = QtWidgets.QLabel(self.centralwidget)
        self.lblViewCoverage_img.setGeometry(QtCore.QRect(390, 440, 111, 121))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.lblViewCoverage_img.setFont(font)
        self.lblViewCoverage_img.setText("")
        self.lblViewCoverage_img.setPixmap(QtGui.QPixmap("view-coverage-white.png"))
        self.lblViewCoverage_img.setScaledContents(True)
        self.lblViewCoverage_img.setObjectName("lblViewCoverage_img")
        self.btnAddUser = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddUser.setGeometry(QtCore.QRect(540, 120, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btnAddUser.setFont(font)
        self.btnAddUser.setStyleSheet("color:#FFFFFF;background-color:rgb(50,0,255);")
        self.btnAddUser.setObjectName("btnAddUser")

        self.btnAddUser.clicked.connect(self.openAddUser)
        
        self.btnAddPolicy = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddPolicy.setGeometry(QtCore.QRect(540, 290, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btnAddPolicy.setFont(font)
        self.btnAddPolicy.setStyleSheet("color:#FFFFFF;background-color:rgb(50,0,255);")
        self.btnAddPolicy.setObjectName("btnAddPolicy")

        self.btnAddPolicy.clicked.connect(self.openAddPolicy)
        
        self.btnViewCoverage = QtWidgets.QPushButton(self.centralwidget)
        self.btnViewCoverage.setGeometry(QtCore.QRect(530, 470, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btnViewCoverage.setFont(font)
        self.btnViewCoverage.setStyleSheet("color:#FFFFFF;background-color:rgb(50,0,255);")
        self.btnViewCoverage.setObjectName("btnViewCoverage")

        self.btnViewCoverage.clicked.connect(self.openViewCoverage)

        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnAddUser.setText(_translate("MainWindow", "Add User"))
        self.btnAddPolicy.setText(_translate("MainWindow", "Add Policy"))
        self.btnViewCoverage.setText(_translate("MainWindow", "View Coverage"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
