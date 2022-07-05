/********************************************************************************
** Form generated from reading UI file 'untitledWkBmAV.ui'
**
** Created by: Qt User Interface Compiler version 5.12.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UNTITLEDWKBMAV_H
#define UNTITLEDWKBMAV_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QWidget>
#include "PySide2extn.RoundProgressBar.h"

QT_BEGIN_NAMESPACE

class Ui_HealthyFork
{
public:
    QWidget *centralwidget;
    QGroupBox *groupBox;
    QTabWidget *tabWidget;
    QWidget *tab;
    roundProgressBar *pbt;
    roundProgressBar *pbr;
    roundProgressBar *pbo;
    roundProgressBar *pbp;
    QLabel *label_2;
    QLabel *label_4;
    QLabel *label_5;
    QLabel *label_6;
    QLabel *label_7;
    QLabel *label_8;
    QLabel *label_14;
    QPushButton *gt;
    QPushButton *go;
    QPushButton *gp;
    QPushButton *gr;
    QWidget *tab_2;
    QLabel *label_9;
    QLabel *label_10;
    QLabel *label_17;
    QLabel *label_18;
    QLabel *pbimc;
    roundProgressBar *pbpeso;
    roundProgressBar *widget_6;
    roundProgressBar *pba;
    QLabel *label_13;
    QLabel *label_19;
    QLabel *label_25;
    QLabel *label_26;
    QWidget *tab_3;
    QLabel *label_11;
    QLabel *label_12;
    QLabel *label_20;
    QLabel *label_21;
    QLineEdit *pass;
    QPushButton *send;
    QLineEdit *ced;
    QLabel *label_22;
    QLabel *label_23;
    QLabel *label_24;
    QLabel *label;
    QLabel *label_3;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *HealthyFork)
    {
        if (HealthyFork->objectName().isEmpty())
            HealthyFork->setObjectName(QString::fromUtf8("HealthyFork"));
        HealthyFork->resize(685, 552);
        centralwidget = new QWidget(HealthyFork);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        groupBox = new QGroupBox(centralwidget);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        groupBox->setGeometry(QRect(60, 80, 571, 471));
        QFont font;
        font.setPointSize(15);
        groupBox->setFont(font);
        groupBox->setStyleSheet(QString::fromUtf8("color:white;"));
        groupBox->setFlat(false);
        tabWidget = new QTabWidget(groupBox);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tabWidget->setGeometry(QRect(0, 20, 571, 431));
        tabWidget->setAutoFillBackground(true);
        tabWidget->setStyleSheet(QString::fromUtf8("color:black;"));
        tabWidget->setTabShape(QTabWidget::Rounded);
        tab = new QWidget();
        tab->setObjectName(QString::fromUtf8("tab"));
        pbt = new roundProgressBar(tab);
        pbt->setObjectName(QString::fromUtf8("pbt"));
        pbt->setGeometry(QRect(60, 100, 120, 80));
        pbr = new roundProgressBar(tab);
        pbr->setObjectName(QString::fromUtf8("pbr"));
        pbr->setGeometry(QRect(380, 100, 120, 80));
        pbo = new roundProgressBar(tab);
        pbo->setObjectName(QString::fromUtf8("pbo"));
        pbo->setGeometry(QRect(60, 250, 120, 80));
        pbp = new roundProgressBar(tab);
        pbp->setObjectName(QString::fromUtf8("pbp"));
        pbp->setGeometry(QRect(380, 250, 120, 80));
        label_2 = new QLabel(tab);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(120, 10, 341, 31));
        label_2->setFont(font);
        label_2->setStyleSheet(QString::fromUtf8("color: #FAFAFA;"));
        label_2->setAlignment(Qt::AlignCenter);
        label_4 = new QLabel(tab);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(70, 70, 101, 16));
        label_4->setStyleSheet(QString::fromUtf8("background-color: #311b92; color:white;"));
        label_4->setAlignment(Qt::AlignCenter);
        label_5 = new QLabel(tab);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(390, 70, 101, 16));
        label_5->setStyleSheet(QString::fromUtf8("background-color: #1a237e; color:white;"));
        label_5->setAlignment(Qt::AlignCenter);
        label_6 = new QLabel(tab);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setGeometry(QRect(80, 230, 75, 16));
        label_6->setStyleSheet(QString::fromUtf8("background-color: #0d47a1; color:white;"));
        label_6->setAlignment(Qt::AlignCenter);
        label_7 = new QLabel(tab);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setGeometry(QRect(400, 230, 75, 16));
        label_7->setStyleSheet(QString::fromUtf8("background-color: #01579b; color:white;"));
        label_7->setAlignment(Qt::AlignCenter);
        label_8 = new QLabel(tab);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setGeometry(QRect(0, 0, 571, 51));
        label_8->setAutoFillBackground(false);
        label_8->setStyleSheet(QString::fromUtf8("background-color: #01579b; color: #4a148c;"));
        label_8->setScaledContents(true);
        label_14 = new QLabel(tab);
        label_14->setObjectName(QString::fromUtf8("label_14"));
        label_14->setGeometry(QRect(0, 370, 571, 31));
        label_14->setPixmap(QPixmap(QString::fromUtf8("../../../Downloads/hand-drawn-abstract-blue-leaves-pattern/5570734.jpg")));
        gt = new QPushButton(tab);
        gt->setObjectName(QString::fromUtf8("gt"));
        gt->setGeometry(QRect(70, 190, 91, 24));
        gt->setStyleSheet(QString::fromUtf8("background-color: #f57f17 ; color:white; border: 0px;"));
        go = new QPushButton(tab);
        go->setObjectName(QString::fromUtf8("go"));
        go->setGeometry(QRect(70, 340, 91, 24));
        go->setStyleSheet(QString::fromUtf8("background-color: #e65100 ; color:white; border: 0px;"));
        gp = new QPushButton(tab);
        gp->setObjectName(QString::fromUtf8("gp"));
        gp->setGeometry(QRect(400, 340, 91, 24));
        gp->setStyleSheet(QString::fromUtf8("background-color: #ffd600 ; color:white; border: 0px;"));
        gr = new QPushButton(tab);
        gr->setObjectName(QString::fromUtf8("gr"));
        gr->setGeometry(QRect(400, 190, 91, 24));
        gr->setStyleSheet(QString::fromUtf8("background-color: #ff6f00 ; color:white; border: 0px;"));
        tabWidget->addTab(tab, QString());
        label_8->raise();
        pbt->raise();
        pbr->raise();
        pbo->raise();
        pbp->raise();
        label_2->raise();
        label_4->raise();
        label_5->raise();
        label_6->raise();
        label_7->raise();
        label_14->raise();
        gt->raise();
        go->raise();
        gp->raise();
        gr->raise();
        tab_2 = new QWidget();
        tab_2->setObjectName(QString::fromUtf8("tab_2"));
        label_9 = new QLabel(tab_2);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setGeometry(QRect(0, 0, 571, 61));
        label_9->setAutoFillBackground(false);
        label_9->setStyleSheet(QString::fromUtf8("background-color: #01579b; color: #01579b;"));
        label_9->setScaledContents(true);
        label_10 = new QLabel(tab_2);
        label_10->setObjectName(QString::fromUtf8("label_10"));
        label_10->setGeometry(QRect(140, 20, 281, 31));
        label_10->setFont(font);
        label_10->setStyleSheet(QString::fromUtf8("color: #FAFAFA;"));
        label_10->setAlignment(Qt::AlignCenter);
        label_17 = new QLabel(tab_2);
        label_17->setObjectName(QString::fromUtf8("label_17"));
        label_17->setGeometry(QRect(40, 130, 101, 16));
        label_17->setStyleSheet(QString::fromUtf8("background-color: #039be5; color:white;"));
        label_17->setAlignment(Qt::AlignCenter);
        label_18 = new QLabel(tab_2);
        label_18->setObjectName(QString::fromUtf8("label_18"));
        label_18->setGeometry(QRect(230, 130, 101, 16));
        label_18->setStyleSheet(QString::fromUtf8("background-color: #00acc1; color:white;"));
        label_18->setAlignment(Qt::AlignCenter);
        pbimc = new QLabel(tab_2);
        pbimc->setObjectName(QString::fromUtf8("pbimc"));
        pbimc->setGeometry(QRect(430, 130, 101, 16));
        pbimc->setStyleSheet(QString::fromUtf8("background-color: #00897b; color:white;"));
        pbimc->setAlignment(Qt::AlignCenter);
        pbpeso = new roundProgressBar(tab_2);
        pbpeso->setObjectName(QString::fromUtf8("pbpeso"));
        pbpeso->setGeometry(QRect(30, 190, 120, 80));
        widget_6 = new roundProgressBar(tab_2);
        widget_6->setObjectName(QString::fromUtf8("widget_6"));
        widget_6->setGeometry(QRect(420, 190, 120, 80));
        pba = new roundProgressBar(tab_2);
        pba->setObjectName(QString::fromUtf8("pba"));
        pba->setGeometry(QRect(220, 190, 120, 80));
        label_13 = new QLabel(tab_2);
        label_13->setObjectName(QString::fromUtf8("label_13"));
        label_13->setGeometry(QRect(0, 375, 571, 31));
        label_13->setPixmap(QPixmap(QString::fromUtf8("../../../Downloads/hand-drawn-abstract-blue-leaves-pattern/5570734.jpg")));
        label_19 = new QLabel(tab_2);
        label_19->setObjectName(QString::fromUtf8("label_19"));
        label_19->setGeometry(QRect(40, 280, 101, 16));
        label_19->setStyleSheet(QString::fromUtf8("background-color: #039be5; color:white;"));
        label_19->setAlignment(Qt::AlignCenter);
        label_25 = new QLabel(tab_2);
        label_25->setObjectName(QString::fromUtf8("label_25"));
        label_25->setGeometry(QRect(230, 280, 101, 16));
        label_25->setStyleSheet(QString::fromUtf8("background-color: #00acc1; color:white;"));
        label_25->setAlignment(Qt::AlignCenter);
        label_26 = new QLabel(tab_2);
        label_26->setObjectName(QString::fromUtf8("label_26"));
        label_26->setGeometry(QRect(430, 280, 101, 16));
        label_26->setStyleSheet(QString::fromUtf8("background-color: #00897b; color:white;"));
        label_26->setAlignment(Qt::AlignCenter);
        tabWidget->addTab(tab_2, QString());
        tab_3 = new QWidget();
        tab_3->setObjectName(QString::fromUtf8("tab_3"));
        label_11 = new QLabel(tab_3);
        label_11->setObjectName(QString::fromUtf8("label_11"));
        label_11->setGeometry(QRect(0, 0, 571, 51));
        label_11->setAutoFillBackground(false);
        label_11->setStyleSheet(QString::fromUtf8("background-color: #0d47a1; color: #4a148c;"));
        label_11->setScaledContents(true);
        label_12 = new QLabel(tab_3);
        label_12->setObjectName(QString::fromUtf8("label_12"));
        label_12->setGeometry(QRect(100, 10, 371, 31));
        QFont font1;
        font1.setPointSize(17);
        font1.setBold(true);
        font1.setItalic(false);
        font1.setWeight(75);
        label_12->setFont(font1);
        label_12->setStyleSheet(QString::fromUtf8("color: #FAFAFA;"));
        label_12->setAlignment(Qt::AlignCenter);
        label_20 = new QLabel(tab_3);
        label_20->setObjectName(QString::fromUtf8("label_20"));
        label_20->setGeometry(QRect(310, 210, 101, 16));
        label_20->setStyleSheet(QString::fromUtf8("background-color:#006064; color:white;"));
        label_20->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        label_21 = new QLabel(tab_3);
        label_21->setObjectName(QString::fromUtf8("label_21"));
        label_21->setGeometry(QRect(310, 300, 101, 16));
        label_21->setStyleSheet(QString::fromUtf8("background-color:#01579b; color:white; border-radius:10;"));
        label_21->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        pass = new QLineEdit(tab_3);
        pass->setObjectName(QString::fromUtf8("pass"));
        pass->setGeometry(QRect(310, 330, 211, 24));
        send = new QPushButton(tab_3);
        send->setObjectName(QString::fromUtf8("send"));
        send->setGeometry(QRect(370, 370, 91, 24));
        send->setStyleSheet(QString::fromUtf8("background-color: #1a237e ; color:white; border: 0px;"));
        ced = new QLineEdit(tab_3);
        ced->setObjectName(QString::fromUtf8("ced"));
        ced->setGeometry(QRect(310, 250, 201, 24));
        label_22 = new QLabel(tab_3);
        label_22->setObjectName(QString::fromUtf8("label_22"));
        label_22->setGeometry(QRect(300, 60, 261, 51));
        QFont font2;
        font2.setPointSize(15);
        font2.setBold(false);
        font2.setItalic(false);
        font2.setWeight(50);
        label_22->setFont(font2);
        label_22->setAutoFillBackground(false);
        label_22->setStyleSheet(QString::fromUtf8("color: white; background-color:#2962ff; "));
        label_22->setTextFormat(Qt::PlainText);
        label_22->setScaledContents(true);
        label_22->setAlignment(Qt::AlignCenter);
        label_22->setWordWrap(true);
        label_23 = new QLabel(tab_3);
        label_23->setObjectName(QString::fromUtf8("label_23"));
        label_23->setGeometry(QRect(20, 60, 271, 331));
        label_23->setPixmap(QPixmap(QString::fromUtf8("../../../Downloads/hand-drawn-abstract-blue-leaves-pattern/5570734.jpg")));
        label_23->setScaledContents(true);
        label_23->setAlignment(Qt::AlignCenter);
        label_24 = new QLabel(tab_3);
        label_24->setObjectName(QString::fromUtf8("label_24"));
        label_24->setGeometry(QRect(310, 130, 231, 51));
        label_24->setAlignment(Qt::AlignCenter);
        label_24->setWordWrap(true);
        tabWidget->addTab(tab_3, QString());
        label = new QLabel(centralwidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(0, 0, 691, 271));
        label->setPixmap(QPixmap(QString::fromUtf8("../../../Downloads/ABSTRACT_COLORFUL_BACKGROUND_01.jpg")));
        label->setScaledContents(true);
        label_3 = new QLabel(centralwidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(230, 40, 251, 31));
        QFont font3;
        font3.setPointSize(20);
        font3.setBold(true);
        font3.setWeight(75);
        label_3->setFont(font3);
        label_3->setStyleSheet(QString::fromUtf8("color: white;"));
        label_3->setAlignment(Qt::AlignCenter);
        HealthyFork->setCentralWidget(centralwidget);
        label->raise();
        label_3->raise();
        groupBox->raise();
        statusbar = new QStatusBar(HealthyFork);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        HealthyFork->setStatusBar(statusbar);

        retranslateUi(HealthyFork);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(HealthyFork);
    } // setupUi

    void retranslateUi(QMainWindow *HealthyFork)
    {
        HealthyFork->setWindowTitle(QApplication::translate("HealthyFork", "Healthy Fork Control", nullptr));
        groupBox->setTitle(QApplication::translate("HealthyFork", "Datos", nullptr));
        label_2->setText(QApplication::translate("HealthyFork", "Datos relacionados Respiraci\303\263n", nullptr));
        label_4->setText(QApplication::translate("HealthyFork", "Temperatura", nullptr));
        label_5->setText(QApplication::translate("HealthyFork", "Respiraci\303\263n", nullptr));
        label_6->setText(QApplication::translate("HealthyFork", "Ox\303\255geno", nullptr));
        label_7->setText(QApplication::translate("HealthyFork", "Pulso", nullptr));
        label_8->setText(QString());
        label_14->setText(QString());
        gt->setText(QApplication::translate("HealthyFork", "Gr\303\241fica", nullptr));
        go->setText(QApplication::translate("HealthyFork", "Gr\303\241fica", nullptr));
        gp->setText(QApplication::translate("HealthyFork", "Gr\303\241fica", nullptr));
        gr->setText(QApplication::translate("HealthyFork", "Gr\303\241fica", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab), QApplication::translate("HealthyFork", "Respiraci\303\263n", nullptr));
        label_9->setText(QString());
        label_10->setText(QApplication::translate("HealthyFork", "Datos relacionados a IMC", nullptr));
        label_17->setText(QApplication::translate("HealthyFork", "Peso", nullptr));
        label_18->setText(QApplication::translate("HealthyFork", "Altura", nullptr));
        pbimc->setText(QApplication::translate("HealthyFork", "IMC", nullptr));
        label_13->setText(QString());
        label_19->setText(QApplication::translate("HealthyFork", "kg", nullptr));
        label_25->setText(QApplication::translate("HealthyFork", "cm", nullptr));
        label_26->setText(QApplication::translate("HealthyFork", "Kg/m\302\262", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_2), QApplication::translate("HealthyFork", "Peso", nullptr));
        label_11->setText(QString());
        label_12->setText(QApplication::translate("HealthyFork", "Formulario de env\303\255o de Datos", nullptr));
        label_20->setText(QApplication::translate("HealthyFork", "C\303\251dula", nullptr));
        label_21->setText(QApplication::translate("HealthyFork", "Contrase\303\261a", nullptr));
        send->setText(QApplication::translate("HealthyFork", "Enviar", nullptr));
        label_22->setText(QApplication::translate("HealthyFork", "Env\303\255o de datos", nullptr));
        label_23->setText(QString());
        label_24->setText(QApplication::translate("HealthyFork", "Porfavor inserte su c\303\251dula y contrase\303\261a para enviar los datos", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_3), QApplication::translate("HealthyFork", "Env\303\255o", nullptr));
        label->setText(QString());
        label_3->setText(QApplication::translate("HealthyFork", "Healthy Fork", nullptr));
    } // retranslateUi

};

namespace Ui {
    class HealthyFork: public Ui_HealthyFork {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UNTITLEDWKBMAV_H
