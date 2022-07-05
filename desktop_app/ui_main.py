
#ifndef UNTITLEDVPNJIC_H
#define UNTITLEDVPNJIC_H

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
    roundProgressBar *widget;
    roundProgressBar *widget_2;
    roundProgressBar *widget_3;
    roundProgressBar *widget_4;
    QLabel *label_2;
    QLabel *label_4;
    QLabel *label_5;
    QLabel *label_6;
    QLabel *label_7;
    QLabel *label_8;
    QLabel *label_13;
    QLabel *label_14;
    QLabel *label_15;
    QLabel *label_16;
    QWidget *tab_2;
    QLabel *label_9;
    QLabel *label_10;
    QLabel *label_17;
    QLabel *label_18;
    QLabel *label_19;
    roundProgressBar *widget_5;
    roundProgressBar *widget_6;
    roundProgressBar *widget_7;
    QWidget *tab_3;
    QLabel *label_11;
    QLabel *label_12;
    QLabel *label_20;
    QLabel *label_21;
    QLineEdit *lineEdit;
    QPushButton *pushButton;
    QLabel *label;
    QLabel *label_3;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *HealthyFork)
    {
        if (HealthyFork->objectName().isEmpty())
            HealthyFork->setObjectName(QString::fromUtf8("HealthyFork"));
        HealthyFork->resize(685, 515);
        centralwidget = new QWidget(HealthyFork);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        groupBox = new QGroupBox(centralwidget);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        groupBox->setGeometry(QRect(60, 80, 571, 391));
        tabWidget = new QTabWidget(groupBox);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tabWidget->setGeometry(QRect(0, 20, 571, 371));
        tabWidget->setAutoFillBackground(true);
        tabWidget->setStyleSheet(QString::fromUtf8("b"));
        tabWidget->setTabShape(QTabWidget::Rounded);
        tab = new QWidget();
        tab->setObjectName(QString::fromUtf8("tab"));
        widget = new roundProgressBar(tab);
        widget->setObjectName(QString::fromUtf8("widget"));
        widget->setGeometry(QRect(60, 100, 120, 80));
        widget_2 = new roundProgressBar(tab);
        widget_2->setObjectName(QString::fromUtf8("widget_2"));
        widget_2->setGeometry(QRect(370, 100, 120, 80));
        widget_3 = new roundProgressBar(tab);
        widget_3->setObjectName(QString::fromUtf8("widget_3"));
        widget_3->setGeometry(QRect(60, 230, 120, 80));
        widget_4 = new roundProgressBar(tab);
        widget_4->setObjectName(QString::fromUtf8("widget_4"));
        widget_4->setGeometry(QRect(370, 230, 120, 80));
        label_2 = new QLabel(tab);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(120, 10, 341, 31));
        QFont font;
        font.setPointSize(15);
        label_2->setFont(font);
        label_2->setStyleSheet(QString::fromUtf8("color: #FAFAFA;"));
        label_2->setAlignment(Qt::AlignCenter);
        label_4 = new QLabel(tab);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(70, 70, 101, 16));
        label_5 = new QLabel(tab);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(390, 70, 101, 16));
        label_6 = new QLabel(tab);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setGeometry(QRect(100, 210, 75, 16));
        label_7 = new QLabel(tab);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setGeometry(QRect(400, 210, 75, 16));
        label_8 = new QLabel(tab);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setGeometry(QRect(0, 0, 571, 51));
        label_8->setAutoFillBackground(false);
        label_8->setStyleSheet(QString::fromUtf8("background-color: #4A148C; color: #4a148c;"));
        label_8->setScaledContents(true);
        label_13 = new QLabel(tab);
        label_13->setObjectName(QString::fromUtf8("label_13"));
        label_13->setGeometry(QRect(200, 130, 101, 16));
        label_14 = new QLabel(tab);
        label_14->setObjectName(QString::fromUtf8("label_14"));
        label_14->setGeometry(QRect(210, 260, 101, 16));
        label_15 = new QLabel(tab);
        label_15->setObjectName(QString::fromUtf8("label_15"));
        label_15->setGeometry(QRect(450, 120, 101, 16));
        label_16 = new QLabel(tab);
        label_16->setObjectName(QString::fromUtf8("label_16"));
        label_16->setGeometry(QRect(470, 260, 101, 16));
        tabWidget->addTab(tab, QString());
        label_8->raise();
        widget->raise();
        widget_2->raise();
        widget_3->raise();
        widget_4->raise();
        label_2->raise();
        label_4->raise();
        label_5->raise();
        label_6->raise();
        label_7->raise();
        label_13->raise();
        label_14->raise();
        label_15->raise();
        label_16->raise();
        tab_2 = new QWidget();
        tab_2->setObjectName(QString::fromUtf8("tab_2"));
        label_9 = new QLabel(tab_2);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setGeometry(QRect(0, 0, 571, 51));
        label_9->setAutoFillBackground(false);
        label_9->setStyleSheet(QString::fromUtf8("background-color: #4A148C; color: #4a148c;"));
        label_9->setScaledContents(true);
        label_10 = new QLabel(tab_2);
        label_10->setObjectName(QString::fromUtf8("label_10"));
        label_10->setGeometry(QRect(130, 10, 281, 31));
        label_10->setFont(font);
        label_10->setStyleSheet(QString::fromUtf8("color: #FAFAFA;"));
        label_10->setAlignment(Qt::AlignCenter);
        label_17 = new QLabel(tab_2);
        label_17->setObjectName(QString::fromUtf8("label_17"));
        label_17->setGeometry(QRect(40, 90, 101, 16));
        label_18 = new QLabel(tab_2);
        label_18->setObjectName(QString::fromUtf8("label_18"));
        label_18->setGeometry(QRect(240, 90, 101, 16));
        label_19 = new QLabel(tab_2);
        label_19->setObjectName(QString::fromUtf8("label_19"));
        label_19->setGeometry(QRect(430, 90, 101, 16));
        widget_5 = new roundProgressBar(tab_2);
        widget_5->setObjectName(QString::fromUtf8("widget_5"));
        widget_5->setGeometry(QRect(30, 160, 120, 80));
        widget_6 = new roundProgressBar(tab_2);
        widget_6->setObjectName(QString::fromUtf8("widget_6"));
        widget_6->setGeometry(QRect(420, 160, 120, 80));
        widget_7 = new roundProgressBar(tab_2);
        widget_7->setObjectName(QString::fromUtf8("widget_7"));
        widget_7->setGeometry(QRect(230, 160, 120, 80));
        tabWidget->addTab(tab_2, QString());
        tab_3 = new QWidget();
        tab_3->setObjectName(QString::fromUtf8("tab_3"));
        label_11 = new QLabel(tab_3);
        label_11->setObjectName(QString::fromUtf8("label_11"));
        label_11->setGeometry(QRect(0, 0, 571, 51));
        label_11->setAutoFillBackground(false);
        label_11->setStyleSheet(QString::fromUtf8("background-color: #4A148C; color: #4a148c;"));
        label_11->setScaledContents(true);
        label_12 = new QLabel(tab_3);
        label_12->setObjectName(QString::fromUtf8("label_12"));
        label_12->setGeometry(QRect(130, 10, 311, 31));
        label_12->setFont(font);
        label_12->setStyleSheet(QString::fromUtf8("color: #FAFAFA;"));
        label_12->setAlignment(Qt::AlignCenter);
        label_20 = new QLabel(tab_3);
        label_20->setObjectName(QString::fromUtf8("label_20"));
        label_20->setGeometry(QRect(220, 90, 101, 16));
        label_21 = new QLabel(tab_3);
        label_21->setObjectName(QString::fromUtf8("label_21"));
        label_21->setGeometry(QRect(220, 140, 101, 16));
        lineEdit = new QLineEdit(tab_3);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        lineEdit->setGeometry(QRect(220, 200, 113, 24));
        pushButton = new QPushButton(tab_3);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(230, 280, 91, 24));
        tabWidget->addTab(tab_3, QString());
        label = new QLabel(centralwidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(0, 0, 691, 271));
        label->setPixmap(QPixmap(QString::fromUtf8("../../../Downloads/ABSTRACT_COLORFUL_BACKGROUND_01.jpg")));
        label->setScaledContents(true);
        label_3 = new QLabel(centralwidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(230, 40, 251, 31));
        QFont font1;
        font1.setPointSize(20);
        font1.setBold(true);
        font1.setWeight(75);
        label_3->setFont(font1);
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
        label_8->setText(QApplication::translate("HealthyFork", "TextLabel", nullptr));
        label_13->setText(QApplication::translate("HealthyFork", "\302\260C", nullptr));
        label_14->setText(QApplication::translate("HealthyFork", "%", nullptr));
        label_15->setText(QApplication::translate("HealthyFork", "RPM", nullptr));
        label_16->setText(QApplication::translate("HealthyFork", "LPM", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab), QApplication::translate("HealthyFork", "Respiraci\303\263n", nullptr));
        label_9->setText(QApplication::translate("HealthyFork", "TextLabel", nullptr));
        label_10->setText(QApplication::translate("HealthyFork", "Datos relacionados a IMC", nullptr));
        label_17->setText(QApplication::translate("HealthyFork", "Peso", nullptr));
        label_18->setText(QApplication::translate("HealthyFork", "Altura", nullptr));
        label_19->setText(QApplication::translate("HealthyFork", "IMC", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_2), QApplication::translate("HealthyFork", "Peso", nullptr));
        label_11->setText(QApplication::translate("HealthyFork", "TextLabel", nullptr));
        label_12->setText(QApplication::translate("HealthyFork", "Formulario de env\303\255o de Datos", nullptr));
        label_20->setText(QApplication::translate("HealthyFork", "Temperatura", nullptr));
        label_21->setText(QApplication::translate("HealthyFork", "Temperatura", nullptr));
        pushButton->setText(QApplication::translate("HealthyFork", "PushButton", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_3), QApplication::translate("HealthyFork", "Env\303\255o", nullptr));
        label->setText(QString());
        label_3->setText(QApplication::translate("HealthyFork", "Healthy Fork", nullptr));
    } // retranslateUi

};

namespace Ui {
    class HealthyFork: public Ui_HealthyFork {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UNTITLEDVPNJIC_H
