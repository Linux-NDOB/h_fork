# worker.py
from PySide2.QtCore import QThread, QObject, Signal, Slot
import time
import json, os, serial
from json.decoder import JSONDecodeError

# Adafruit
from Adafruit_IO import *
aio = Client('SirAstolf','aio_SFgP65PgaZ2bTOcuKQt60KO9t42o')

class Imc(QObject):
    finished = Signal()
    second_data = Signal(float,float, float)

    @Slot()
    def procCounter(self): # A slot takes no params
        while True:
            try:
                arduino_port = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)
                time.sleep(1)
                if arduino_port.isOpen():
                    while arduino_port.inWaiting() == 0: pass
                    if arduino_port.inWaiting() > 0:
                        write_json = open('h&w.json', 'w')
                        for i in range(5):
                            line = arduino_port.readline().rstrip().decode('utf-8')
                            write_json.write(line)
                            print(line.strip())
                            #time.sleep(0.1)
                        write_json.close()

                        # READ JSON
                        filesize = os.path.getsize('h&w.json')

                        if filesize == 0:

                            # self.intReady.emit(1.0, 1.0, 1.0, 1.0)
                            print("Empty file")

                        else:
                            with open("h&w.json") as data_json:
                                obj_json = json.load(data_json)
                                data_json.close()

                            height = obj_json["Height"]
                            weight = obj_json["Weight"]
                            imc = obj_json["IMC"]


                            self.second_data.emit(height, weight, imc)
                            time.sleep(1)
                            #aio.send("healthypi.heartrate", str(h_rate))
                            #aio.send("healthypi.spo2", str(oxigen))
                            #aio.send("healthypi.temperature", str(temperature))
                            #aio.send("healthypi.respiration", str(resp_rate))
                            #time.sleep(1)

                        self.finished.emit()

                arduino_port = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
                time.sleep(1)
                if arduino_port.isOpen():
                    while arduino_port.inWaiting() == 0: pass
                    if arduino_port.inWaiting() > 0:
                        write_json = open('h&w.json', 'w')
                        for i in range(5):
                            line = arduino_port.readline().rstrip().decode('utf-8')
                            write_json.write(line)
                            print(line.strip())
                            # time.sleep(0.1)
                        write_json.close()

                        # READ JSON
                        filesize = os.path.getsize('h&w.json')

                        if filesize == 0:

                            # self.intReady.emit(1.0, 1.0, 1.0, 1.0)
                            print("Empty file")

                        else:
                            with open("h&w.json") as data_json:
                                obj_json = json.load(data_json)
                                data_json.close()

                            height = obj_json["Height"]
                            weight = obj_json["Weight"]
                            imc = obj_json["IMC"]

                            self.second_data.emit(height, weight, imc)
                            time.sleep(1)
                            # aio.send("healthypi.heartrate", str(h_rate))
                            # aio.send("healthypi.spo2", str(oxigen))
                            # aio.send("healthypi.temperature", str(temperature))
                            # aio.send("healthypi.respiration", str(resp_rate))
                            # time.sleep(1)

                        self.finished.emit()
                else:
                    print("not found")

            except  serial.SerialException as e:
                print(e)

            except KeyboardInterrupt as e:
                print(e)









