import sys
import time
from bd import Mongo
from Sensor import Sensor
from Adafruit import Adafruit
from lcd.lcd_ecologic import lcd_ecologic

class Menu:
    def __init__(self):
        self._mongo = Mongo()
        self._sensor = Sensor()
        self._adafruit = Adafruit()
        self._lcd = lcd_ecologic()
    
    def leerSensorTyH(self):
        try:
            self._sensor.lectura()
            self._mongo.insertarDatos(self._sensor.getTemperatura(),self._sensor.getHumedad(), self._sensor.getHumedadPlanta(), self._sensor.getFecha())
            #self._mongo.insertarDatos(self._sensor.getTemperatura(),self._sensor.getHumedad(), 30.2, self._sensor.getFecha())
            print()
            print('Temperatura={0:0.1f}* Humedad={1:0.1f}%'.format(self._sensor.getTemperatura(), self._sensor.getHumedad()))
            print('Humedad_planta={0}'.format(self._sensor.getHumedadPlanta()))
            print('Fecha={0}'.format(self._sensor.getFecha()))
        except:
            sys.exit(1)
            
    def publicaDatos(self):
        self._adafruit.publicarHumedad(self._sensor.getHumedad())
        self._adafruit.publicarTemperatura(self._sensor.getTemperatura())
        self._adafruit.publicarHumedadPlanta(self._sensor.getHumedadPlanta())
        #self._adafruit.publicarHumedadPlanta(30.2)
        
    def imprimeDatos(self):
        self._lcd.imprimirPantalla(self._sensor.getHumedad(), self._sensor.getTemperatura(), self._sensor.getHumedadPlanta(), self._sensor.getFecha())
        #self._lcd.imprimirPantalla(self._sensor.getHumedad(), self._sensor.getTemperatura(), 30.2, self._sensor.getFecha())
        
    def run(self):
        try:
            while True:
                self.leerSensorTyH()
                self.publicaDatos()
                self.imprimeDatos()
                time.sleep(10)
            else:
                print("Tiempo excedido")

        except KeyboardInterrupt:
            print('Pantalla limpiada')
            self._lcd.limpiarPantalla()
