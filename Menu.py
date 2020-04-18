import sys
import time
from bd import Mongo
from Sensor import Sensor
from Adafruit import Adafruit
from lcd.lcd_ecologic import lcd_ecologic
from LED import LED
from Firebase import Firebase

class Menu:
    def __init__(self):
        self._mongo = Mongo()
        self._sensor = Sensor()
        self._adafruit = Adafruit()
        self._lcd = lcd_ecologic()
        self._led = LED()
        self._firebase  = Firebase()
    
    def leerSensores(self):
        try:
            self._sensor.lectura()
            print()
            print('Temperatura={0:0.1f}° Humedad={1:0.1f}%'.format(self._sensor.getTemperatura(), self._sensor.getHumedad()))
            print('Humedad_planta={0} LDR={1}'.format(self._sensor.getHumedadPlanta(), self._sensor.getLDR()))
            print('Fecha={0}'.format(self._sensor.getFecha()))
        except:
            sys.exit(1)
            
    def publicaDatos(self):
        self._adafruit.publicarHumedad(self._sensor.getHumedad())
        self._adafruit.publicarTemperatura(self._sensor.getTemperatura())
        self._adafruit.publicarHumedadPlanta(self._sensor.getHumedadPlanta())
        self._adafruit.publicarLDR(self._sensor.getLDR())
        self._firebase.insertaSensores(self._sensor.getTemperatura(), self._sensor.getHumedad(), self._sensor.getLDR(), self._sensor.getHumedadPlanta(), self._sensor.getFecha())
        
    def imprimeDatos(self):
        self._led.encenderLED(self._sensor.getHumedadPlanta())
        self._lcd.imprimirPantalla(self._sensor.getHumedad(), self._sensor.getTemperatura(), self._sensor.getHumedadPlanta(), self._sensor.getLDR(), self._sensor.getFecha())
        
    def guardaDatos(self):
        self._mongo.consultarCantidadRegistros()
        self._mongo.insertarDatos(self._sensor.getTemperatura(),self._sensor.getHumedad(), self._sensor.getHumedadPlanta(), self._sensor.getLDR(), self._sensor.getFecha())
        
    def run(self):
        try:
            while True:
                self.leerSensores()
                self.guardaDatos()
                self.publicaDatos()
                self.imprimeDatos()
                time.sleep(10)
            else:
                print("Tiempo excedido")
        except KeyboardInterrupt:
            print('Pantalla limpiada')
            self._lcd.limpiarPantalla()
            print('LEDs limpiados')
            self._led.limpiarLED()
