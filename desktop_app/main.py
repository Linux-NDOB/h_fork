import sys
import mysql.connector
from datetime import datetime as date
import sys, serial, time, json, math, worker
import PySide2

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QPen)
from PySide2.QtWidgets import *

# IMPORT PYSIDE2EXTN WIDGET YOU USED IN THE QTDESIGNER FOR DESIGNING.
from PySide2extn.RoundProgressBar import roundProgressBar

# UI FILE CONVERTED FROM .ui to python file ui.py
from ui_mainwindow import *


class MainWindow(QMainWindow):

    def onIntReady(self, temperature, oxigen, h_rate, resp_rate):
         # Imported from worker vars
        self.ui.pbt.rpb_textValue = str(temperature)
        self.ui.pbo.rpb_textValue = str(oxigen)
        self.ui.pbp.rpb_textValue = str(h_rate)
        self.ui.pbr.rpb_textValue = str(resp_rate)

        #self.ui.pbo.rpb_setValue(int(oxigen))
        #self.ui.pbp.rpb_setValue(int(h_rate))
        #self.ui.pbr.rpb_setValue(int(resp_rate))

         #rpb_textValue

        self.atemp = temperature
        self.aox = oxigen
        self.ah_rate = h_rate
        self.a_rate = resp_rate

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_HealthyFork()
        self.ui.setupUi(self)

        self.ui.pbt.rpb_setMaximum(100)
        self.ui.pbo.rpb_setMaximum(150)
        self.ui.pbr.rpb_setMaximum(200)
        self.ui.pbp.rpb_setMaximum(200)
        self.ui.pbpeso.rpb_setMaximum(200)
        #self.ui.pbimc.rpb_setMaximum(420)

        self.ui.send.clicked.connect(self.send_data)




        # 1 - create Worker and Thread inside the Form
        self.obj = worker.Worker()  # no parent!
        self.thread = PySide2.QtCore.QThread()  # no parent!

        # 2 - Connect Worker`s Signals to Form method slots to post data.
        self.obj.intReady.connect(self.onIntReady)

        # 3 - Move the Worker object to the Thread object
        self.obj.moveToThread(self.thread)

        # 4 - Connect Worker Signals to the Thread slots
        self.obj.finished.connect(self.thread.quit)

        # 5 - Connect Thread started signal to Worker operational slot method
        self.thread.started.connect(self.obj.procCounter)

        # * - Thread finished signal will close the app if you want!
        # self.thread.finished.connect(app.exit)

        # 6 - Start the thread
        self.thread.start()

    def send_data(self):
        cedula = int(self.ui.ced.text())

        day = int(date.today().strftime("%w"))

        year = int(date.today().strftime("%Y"))

        month = int(date.today().strftime("%m"))

        hour = int(date.today().strftime("%H"))

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='h_fork',
                                                 user='root',
                                                 password='kodokushi')

            mySql_insert_query = """INSERT INTO vital_signs ( patient_id, oxigen, heart_rate, temperature, resp_rate, weight, height, day_taken, year_taken, month_taken, hour_taken)
                                   VALUES 
                                   (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

            record = (cedula, self.aox, self.ah_rate, self.atemp, self.a_rate, 100, 80, day, year, month, hour )


            cursor = connection.cursor()
            cursor.execute(mySql_insert_query, record)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into table")

            dlg = QMessageBox(self)
            dlg.setWindowTitle("Correcto!")
            dlg.setText("Los datos de registro se han ennviado correctamente a su cédula")
            button = dlg.exec()

            if button == QMessageBox.Ok:
                print("OK!")

            cursor.close()

        except mysql.connector.Error as error:
            print("Failed to insert record into table {}".format(error))

        finally:
            if connection.is_connected():
                connection.close()
                print("MySQL connection is closed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

