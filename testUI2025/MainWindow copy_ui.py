# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow copy.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(733, 205)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(460, 80, 31, 31))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 80, 31, 41))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 30, 31, 41))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 30, 31, 41))
        self.label_4.setFont(font)
        self.lcd_resultado = QLCDNumber(self.centralwidget)
        self.lcd_resultado.setObjectName(u"lcd_resultado")
        self.lcd_resultado.setGeometry(QRect(490, 60, 231, 71))
        font1 = QFont()
        font1.setPointSize(18)
        self.lcd_resultado.setFont(font1)
        self.btn_suma = QPushButton(self.centralwidget)
        self.btn_suma.setObjectName(u"btn_suma")
        self.btn_suma.setGeometry(QRect(180, 140, 121, 41))
        self.btn_suma.setFont(font)
        self.te_valor1 = QTextEdit(self.centralwidget)
        self.te_valor1.setObjectName(u"te_valor1")
        self.te_valor1.setGeometry(QRect(20, 70, 201, 51))
        self.te_valor1.setFont(font)
        self.te_valor2 = QTextEdit(self.centralwidget)
        self.te_valor2.setObjectName(u"te_valor2")
        self.te_valor2.setGeometry(QRect(260, 70, 201, 51))
        self.te_valor2.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.btn_suma.setText(QCoreApplication.translate("MainWindow", u"SUMAR", None))
    # retranslateUi

