# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desk_app.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar
from pyqtgraph import PlotWidget


class Ui_HealthyFork(object):
    def setupUi(self, HealthyFork):
        if not HealthyFork.objectName():
            HealthyFork.setObjectName(u"HealthyFork")
        HealthyFork.resize(690, 552)
        self.centralwidget = QWidget(HealthyFork)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(60, 80, 571, 471))
        font = QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"color:white;")
        self.groupBox.setFlat(False)
        self.tabWidget = QTabWidget(self.groupBox)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 20, 571, 431))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet(u"color:black;")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.pbt = roundProgressBar(self.tab)
        self.pbt.setObjectName(u"pbt")
        self.pbt.setGeometry(QRect(80, 100, 120, 80))
        self.pbr = roundProgressBar(self.tab)
        self.pbr.setObjectName(u"pbr")
        self.pbr.setGeometry(QRect(400, 100, 120, 80))
        self.pbo = roundProgressBar(self.tab)
        self.pbo.setObjectName(u"pbo")
        self.pbo.setGeometry(QRect(80, 250, 120, 80))
        self.pbp = roundProgressBar(self.tab)
        self.pbp.setObjectName(u"pbp")
        self.pbp.setGeometry(QRect(400, 260, 120, 80))
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 10, 351, 31))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: #FAFAFA;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 70, 101, 16))
        self.label_4.setStyleSheet(u"background-color: #311b92; color:white;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(390, 70, 101, 16))
        self.label_5.setStyleSheet(u"background-color: #1a237e; color:white;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 230, 75, 16))
        self.label_6.setStyleSheet(u"background-color: #0d47a1; color:white;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(400, 230, 75, 16))
        self.label_7.setStyleSheet(u"background-color: #01579b; color:white;")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 0, 571, 51))
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet(u"background-color:#aa00ff;")
        self.label_8.setScaledContents(True)
        self.label_14 = QLabel(self.tab)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 381, 571, 20))
        self.label_14.setPixmap(QPixmap(u"../../../Downloads/wallpaperbetter.com_1366x768.jpg"))
        self.tabWidget.addTab(self.tab, "")
        self.label_8.raise_()
        self.pbt.raise_()
        self.pbr.raise_()
        self.pbo.raise_()
        self.pbp.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_14.raise_()
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 571, 61))
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet(u"background-color: #01579b; color: #01579b;")
        self.label_9.setScaledContents(True)
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(140, 20, 281, 31))
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"color: #FAFAFA;")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_17 = QLabel(self.tab_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(40, 130, 101, 16))
        self.label_17.setStyleSheet(u"background-color: #039be5; color:white;")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(230, 130, 101, 16))
        self.label_18.setStyleSheet(u"background-color: #00acc1; color:white;")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.pbimc = QLabel(self.tab_2)
        self.pbimc.setObjectName(u"pbimc")
        self.pbimc.setGeometry(QRect(430, 130, 101, 16))
        self.pbimc.setStyleSheet(u"background-color: #00897b; color:white;")
        self.pbimc.setAlignment(Qt.AlignCenter)
        self.pbpeso = roundProgressBar(self.tab_2)
        self.pbpeso.setObjectName(u"pbpeso")
        self.pbpeso.setGeometry(QRect(40, 180, 120, 80))
        self.pbimc_2 = roundProgressBar(self.tab_2)
        self.pbimc_2.setObjectName(u"pbimc_2")
        self.pbimc_2.setGeometry(QRect(440, 180, 120, 80))
        self.pba = roundProgressBar(self.tab_2)
        self.pba.setObjectName(u"pba")
        self.pba.setGeometry(QRect(240, 180, 120, 80))
        self.label_13 = QLabel(self.tab_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 375, 571, 31))
        self.label_13.setPixmap(QPixmap(u"../../../Downloads/hand-drawn-abstract-blue-leaves-pattern/5570734.jpg"))
        self.label_19 = QLabel(self.tab_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(40, 280, 101, 16))
        self.label_19.setStyleSheet(u"background-color: #039be5; color:white;")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_25 = QLabel(self.tab_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(230, 280, 101, 16))
        self.label_25.setStyleSheet(u"background-color: #00acc1; color:white;")
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_26 = QLabel(self.tab_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(430, 280, 101, 16))
        self.label_26.setStyleSheet(u"background-color: #00897b; color:white;")
        self.label_26.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_11 = QLabel(self.tab_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 0, 571, 51))
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet(u"background-color: #0d47a1; color: #4a148c;")
        self.label_11.setScaledContents(True)
        self.label_12 = QLabel(self.tab_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(100, 10, 371, 31))
        font2 = QFont()
        font2.setPointSize(17)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"color: #FAFAFA;")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_20 = QLabel(self.tab_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(310, 210, 101, 16))
        self.label_20.setStyleSheet(u"background-color:#006064; color:white;")
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_21 = QLabel(self.tab_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(310, 300, 101, 16))
        self.label_21.setStyleSheet(u"background-color:#01579b; color:white; border-radius:10;")
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.passw = QLineEdit(self.tab_3)
        self.passw.setObjectName(u"passw")
        self.passw.setGeometry(QRect(310, 330, 211, 24))
        self.send = QPushButton(self.tab_3)
        self.send.setObjectName(u"send")
        self.send.setGeometry(QRect(370, 370, 91, 24))
        self.send.setStyleSheet(u"background-color: #1a237e ; color:white; border: 0px;")
        self.ced = QLineEdit(self.tab_3)
        self.ced.setObjectName(u"ced")
        self.ced.setGeometry(QRect(310, 250, 211, 24))
        self.label_22 = QLabel(self.tab_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(300, 60, 261, 51))
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.label_22.setFont(font3)
        self.label_22.setAutoFillBackground(False)
        self.label_22.setStyleSheet(u"color: white; background-color:#2962ff; ")
        self.label_22.setTextFormat(Qt.PlainText)
        self.label_22.setScaledContents(True)
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_22.setWordWrap(True)
        self.label_23 = QLabel(self.tab_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 60, 271, 331))
        self.label_23.setPixmap(QPixmap(u"../../../Downloads/hand-drawn-abstract-blue-leaves-pattern/5570734.jpg"))
        self.label_23.setScaledContents(True)
        self.label_23.setAlignment(Qt.AlignCenter)
        self.label_24 = QLabel(self.tab_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(310, 130, 231, 51))
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_24.setWordWrap(True)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.t_graph = PlotWidget(self.tab_4)
        self.t_graph.setObjectName(u"t_graph")
        self.t_graph.setGeometry(QRect(20, 40, 531, 341))
        self.label_15 = QLabel(self.tab_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(250, 10, 101, 16))
        self.tabWidget.addTab(self.tab_4, "")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 691, 321))
        self.label.setPixmap(QPixmap(u"../../../Downloads/wallpaperbetter.com_1366x768.jpg"))
        self.label.setScaledContents(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 40, 251, 31))
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color: white;")
        self.label_3.setAlignment(Qt.AlignCenter)
        HealthyFork.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.label_3.raise_()
        self.groupBox.raise_()
        self.statusbar = QStatusBar(HealthyFork)
        self.statusbar.setObjectName(u"statusbar")
        HealthyFork.setStatusBar(self.statusbar)

        self.retranslateUi(HealthyFork)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(HealthyFork)
    # setupUi

    def retranslateUi(self, HealthyFork):
        HealthyFork.setWindowTitle(QCoreApplication.translate("HealthyFork", u"Healthy Fork Control", None))
        self.groupBox.setTitle(QCoreApplication.translate("HealthyFork", u"Datos", None))
        self.label_2.setText(QCoreApplication.translate("HealthyFork", u"Respiraci\u00f3n", None))
        self.label_4.setText(QCoreApplication.translate("HealthyFork", u"Temperatura", None))
        self.label_5.setText(QCoreApplication.translate("HealthyFork", u"Respiraci\u00f3n", None))
        self.label_6.setText(QCoreApplication.translate("HealthyFork", u"Ox\u00edgeno", None))
        self.label_7.setText(QCoreApplication.translate("HealthyFork", u"Pulso", None))
        self.label_8.setText("")
        self.label_14.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("HealthyFork", u"Respiraci\u00f3n", None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("HealthyFork", u"IMC", None))
        self.label_17.setText(QCoreApplication.translate("HealthyFork", u"Peso", None))
        self.label_18.setText(QCoreApplication.translate("HealthyFork", u"Altura", None))
        self.pbimc.setText(QCoreApplication.translate("HealthyFork", u"IMC", None))
        self.label_13.setText("")
        self.label_19.setText(QCoreApplication.translate("HealthyFork", u"kg", None))
        self.label_25.setText(QCoreApplication.translate("HealthyFork", u"cm", None))
        self.label_26.setText(QCoreApplication.translate("HealthyFork", u"Kg/m\u00b2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("HealthyFork", u"Peso", None))
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("HealthyFork", u"Formulario de env\u00edo de Datos", None))
        self.label_20.setText(QCoreApplication.translate("HealthyFork", u"C\u00e9dula", None))
        self.label_21.setText(QCoreApplication.translate("HealthyFork", u"Contrase\u00f1a", None))
        self.send.setText(QCoreApplication.translate("HealthyFork", u"Enviar", None))
        self.label_22.setText(QCoreApplication.translate("HealthyFork", u"Env\u00edo de datos", None))
        self.label_23.setText("")
        self.label_24.setText(QCoreApplication.translate("HealthyFork", u"Porfavor inserte su c\u00e9dula y contrase\u00f1a para enviar los datos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("HealthyFork", u"Env\u00edo", None))
        self.label_15.setText(QCoreApplication.translate("HealthyFork", u"Temperatura", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("HealthyFork", u"G\u0155aficas", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("HealthyFork", u"Healthy Fork", None))
    # retranslateUi

