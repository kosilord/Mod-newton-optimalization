# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(737, 698)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Eps1 = QtWidgets.QLineEdit(self.centralwidget)
        self.Eps1.setGeometry(QtCore.QRect(60, 40, 111, 21))
        self.Eps1.setObjectName("Eps1")
        self.Eps2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Eps2.setGeometry(QtCore.QRect(60, 70, 111, 21))
        self.Eps2.setObjectName("Eps2")
        self.Eps3 = QtWidgets.QLineEdit(self.centralwidget)
        self.Eps3.setGeometry(QtCore.QRect(60, 100, 111, 21))
        self.Eps3.setObjectName("Eps3")
        self.Beta = QtWidgets.QLineEdit(self.centralwidget)
        self.Beta.setGeometry(QtCore.QRect(380, 90, 161, 21))
        self.Beta.setObjectName("Beta")
        self.tau = QtWidgets.QLineEdit(self.centralwidget)
        self.tau.setGeometry(QtCore.QRect(380, 120, 161, 21))
        self.tau.setObjectName("tau")
        self.L = QtWidgets.QLineEdit(self.centralwidget)
        self.L.setGeometry(QtCore.QRect(60, 130, 111, 21))
        self.L.setObjectName("L")
        self.oblicz = QtWidgets.QPushButton(self.centralwidget)
        self.oblicz.setGeometry(QtCore.QRect(580, 90, 111, 51))
        self.oblicz.setObjectName("oblicz")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 490, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 0, 121, 41))
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 51, 41))
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 51, 41))
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 51, 41))
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 120, 31, 41))
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(280, -20, 361, 111))
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(330, 80, 51, 41))
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(340, 110, 51, 41))
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 160, 171, 31))
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 200, 91, 31))
        self.label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 240, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.funkcja = QtWidgets.QLineEdit(self.centralwidget)
        self.funkcja.setGeometry(QtCore.QRect(90, 200, 611, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.funkcja.setFont(font)
        self.funkcja.setObjectName("funkcja")
        self.punkty_p = QtWidgets.QLineEdit(self.centralwidget)
        self.punkty_p.setGeometry(QtCore.QRect(170, 160, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.punkty_p.setFont(font)
        self.punkty_p.setObjectName("punkty_p")
        self.Logi = QtWidgets.QTextBrowser(self.centralwidget)
        self.Logi.setGeometry(QtCore.QRect(10, 270, 251, 371))
        self.Logi.setObjectName("Logi")
        self.box = QtWidgets.QGroupBox(self.centralwidget)
        self.box.setGeometry(QtCore.QRect(280, 270, 421, 371))
        self.box.setTitle("")
        self.box.setObjectName("box")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(280, 240, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 737, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Eps1.setText(_translate("MainWindow", "0.001"))
        self.Eps2.setText(_translate("MainWindow", "0.001"))
        self.Eps3.setText(_translate("MainWindow", "0.001"))
        self.Beta.setText(_translate("MainWindow", "2/5"))
        self.tau.setText(_translate("MainWindow", "5"))
        self.L.setText(_translate("MainWindow", "1000"))
        self.oblicz.setText(_translate("MainWindow", "Oblicz !"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Kryteria stopu:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Eps1 : </span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Eps2 : </span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Eps3 : </span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">L    : </span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Parametry algorytmu minimum w kierunku </span></p><p align=\"center\"><span style=\" font-size:14pt;\">testu Goldsteina:</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">beta :</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">tau :</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Punkt początkowy:</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">  Funkcja:</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "Przebieg działania algorytmu:"))
        self.funkcja.setText(_translate("MainWindow", "(x1-2)**2 + (x2-1)**2"))
        self.punkty_p.setText(_translate("MainWindow", "6.5, -6"))
        self.Logi.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sposób wprowadzania Punktów początkowych</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> np : 6, -6 </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Zmienne w funkcji</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">wprowadzamy jako x1 , x2, x3 ...</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Przycisk Oblicz uruchamia kod programu.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "Wykres Funkcji :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
