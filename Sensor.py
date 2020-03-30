import serial
import Adafruit_DHT
from datetime import datetime

class Sensor:
    
    def __init__(self):
        self._sensor = Adafruit_DHT.DHT11
        self._pin = 13
        self._arduino = serial.Serial('/dev/ttyACM0',9600)
        
    def lectura(self):
        now = datetime.now()
        self._fecha = now.strftime("%Y-%m-%d (%H:%M:%S)")
        self._humedad, self._temperatura = Adafruit_DHT.read_retry(self._sensor, self._pin)
        lectura = self._arduino.readline()
        self._humedadPlanta = int(lectura)
        self._humedadPlanta = float(self._humedadPlanta /10)
        #print(self._humedadPlanta)
        
    def getTemperatura(self):
        return self._temperatura
    
    def getHumedad(self):
        return self._humedad
    
    def getFecha(self):
        return self._fecha
    
    def getHumedadPlanta(self):
        return self._humedadPlanta