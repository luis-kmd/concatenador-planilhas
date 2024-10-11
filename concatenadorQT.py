# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'concatenadorQT.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(418, 321)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setStyleStrategy(QFont.NoAntialias)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet(u"\n"
"    background-color: qlineargradient(\n"
"        spread: pad, x1: 0, y1: 0, x2: 1, y2: 1,\n"
"        stop: 0 #8B0000, stop: 1 #B22222\n"
"    );\n"
"    color: white;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.selecionarExcel = QPushButton(self.centralwidget)
        self.selecionarExcel.setObjectName(u"selecionarExcel")
        self.selecionarExcel.setGeometry(QRect(50, 50, 141, 41))
        font1 = QFont()
        font1.setFamilies([u"Malgun Gothic"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.selecionarExcel.setFont(font1)
        self.selecionarExcel.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"color: black;")
        self.barraProgresso = QProgressBar(self.centralwidget)
        self.barraProgresso.setObjectName(u"barraProgresso")
        self.barraProgresso.setGeometry(QRect(50, 270, 321, 23))
        self.barraProgresso.setFont(font1)
        self.barraProgresso.setStyleSheet(u"color: black;")
        self.barraProgresso.setValue(24)
        self.barraProgresso.setAlignment(Qt.AlignCenter)
        self.log = QTextEdit(self.centralwidget)
        self.log.setObjectName(u"log")
        self.log.setGeometry(QRect(50, 110, 321, 131))
        font2 = QFont()
        font2.setFamilies([u"Malgun Gothic"])
        font2.setPointSize(9)
        font2.setBold(True)
        self.log.setFont(font2)
        self.log.setStyleSheet(u"color: white;")
        self.executar = QPushButton(self.centralwidget)
        self.executar.setObjectName(u"executar")
        self.executar.setGeometry(QRect(270, 50, 101, 41))
        self.executar.setFont(font1)
        self.executar.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"color: black;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 0, 281, 51))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: white;\n"
"background-color: transparent;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.selecionarExcel.setText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio", None))
        self.executar.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Concatenador de planilhas</span></p></body></html>", None))
    # retranslateUi

