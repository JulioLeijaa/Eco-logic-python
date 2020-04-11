from Adafruit_IO import Client
from bd import Mongo
import sys
import RPi.GPIO as GPIO
import time

class Adafruit:
    def __init__(self):
        self.aio = Client('Cesar_utt', '05037193ee4a460eb2e5ba8bc1e91a45')
        self._pinBomba = 6
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._pinBomba, GPIO.OUT)
        GPIO.setwarnings(False)
        GPIO.output(self._pinBomba, GPIO.LOW)
        self._mongo = Mongo()
        
    def subBomba(self):
        try:
            data = self.aio.receive('bomba')
            if data.value == 'ON':
                print("El valor es: {0} (10 segundos)".format(data.value))
                GPIO.output(self._pinBomba, GPIO.HIGH)
                time.sleep(10)
                GPIO.output(self._pinBomba, GPIO.LOW)
                self.aio.send_data('bomba','OFF')
                self._mongo.consultarCantidadRegistros()
                self._mongo.insertarDatos(10)
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
                GPIO.output(self._pinBomba, GPIO.HIGH)
                time.sleep(seg)
                GPIO.output(self._pinBomba, GPIO.LOW)
                self.aio.send_data('bombatiempo','0')
                self._mongo.consultarCantidadRegistros()
                self._mongo.insertarDatos(seg)
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