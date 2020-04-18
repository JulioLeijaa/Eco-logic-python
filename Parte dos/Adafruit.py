from Adafruit_IO import Client
from bd import Mongo
import sys
import RPi.GPIO as GPIO
import time
from Firebase import Firebase
import time
from datetime import datetime

class Adafruit:
    def __init__(self):
        self.aio = Client('Cesar_utt', '05037193ee4a460eb2e5ba8bc1e91a45')
        self._pinBomba = 6
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._pinBomba, GPIO.OUT)
        GPIO.setwarnings(False)
        self._mongo = Mongo()
        self._firebase = Firebase()
        
    def subBomba(self):
        try:
            data = self.aio.receive('bomba')
            if data.value == 'ON':
                print("El valor es: {0} (10 segundos)".format(data.value))
                GPIO.output(self._pinBomba, GPIO.LOW)
                time.sleep(10)
                GPIO.output(self._pinBomba, GPIO.HIGH)
                self.aio.send_data('bomba','OFF')
                self._mongo.consultarCantidadRegistros()
                now = datetime.now() #se declara objeto de fecha
                self._fecha = now.strftime("%Y-%m-%d (%H:%M:%S)") #formato de la fecha #print(self._fecha)
                self._mongo.insertarDatos(10, self._fecha)
                self._firebase.insertaBomba(10, self._fecha)
                print('Se envió OFF a Adafruit')
            #elif data.value == 'OFF':
                #print("El valor es {0}".format(data.value))
        except KeyboardInterrupt:
            sys.exit(1)
        except:
            print('Fallo al obtener datos')

    def subBombaTiempo(self):
        try:
            data = self.aio.receive('bombatiempo')
            if int(data.value) >= 10:
                print("El valor es: {0} segundos".format(data.value))
                seg = int(data.value)
                GPIO.output(self._pinBomba, GPIO.LOW)
                time.sleep(seg)
                GPIO.output(self._pinBomba, GPIO.HIGH)
                self.aio.send_data('bombatiempo','0')
                self._mongo.consultarCantidadRegistros()
                now = datetime.now() #se declara objeto de fecha
                self._fecha = now.strftime("%Y-%m-%d (%H:%M:%S)") #formato de la fecha #print(self._fecha)
                self._mongo.insertarDatos(seg, self._fecha)
                self._firebase.insertaBomba(seg, self._fecha)
                print('Se envió 0 a Adafruit')
            #elif int(data.value) < 10:
                #print('El valor debe ser mayor a 10')
                #print('Valor = {0}'.format(data.value))
            #elif data.value == '0':
                #print("El valor es {0}".format(data.value))
        except KeyboardInterrupt:
            sys.exit(1)
        except:
            print('Fallo al obtener datos')