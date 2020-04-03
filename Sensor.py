import serial
import time
import simplejson as json
import Adafruit_DHT
from datetime import datetime

class Sensor:
    
    def __init__(self):
        self._sensor = Adafruit_DHT.DHT11 #declaración de sensor de temperatura
        self._pin = 13 #pin de sensor de temperatura
        self._arduino = serial.Serial('/dev/ttyACM0',9600) #declaración de puerto serial
        
    def lectura(self):
        now = datetime.now() #se declara objeto de fecha
        self._fecha = now.strftime("%Y-%m-%d (%H:%M:%S)") #formato de la fecha #print(self._fecha)
        self._humedad, self._temperatura = Adafruit_DHT.read_retry(self._sensor, self._pin) #lectura de temperatura y humedad #print(self._temperatura)
        lectura = self._arduino.readline() #lectura de arduino por USB0
        print(lectura)
        data = json.loads(lectura) #codificación a json #print(data)
        self._humedadPlanta = int(data["hum"]) #print(self._humedadPlanta)
        self._humedadPlanta = float(self._humedadPlanta /10) #print(self._humedadPlanta)
        self._ldr = int(data["ldr"]) #print(self._ldr)
        self._ldr = float(self._ldr /10) #print(self._ldr)
        
    def getTemperatura(self):
        return self._temperatura
    
    def getHumedad(self):
        return self._humedad
    
    def getFecha(self):
        return self._fecha
    
    def getHumedadPlanta(self):
        return self._humedadPlanta
    
    def getLDR(self):
        return self._ldr