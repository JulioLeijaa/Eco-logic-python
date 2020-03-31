import RPi.GPIO as GPIO

class LED:
    
    def __init__(self):
        self._pinRojo = 20
        self._pinVerde =21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._pinRojo, GPIO.OUT)
        GPIO.setup(self._pinVerde, GPIO.OUT)
    
    def encenderLED(self, humedadPlanta):
        if humedadPlanta <= 50:
            GPIO.output(self._pinVerde, GPIO.HIGH)
            GPIO.output(self._pinRojo, GPIO.LOW)
        else:
            GPIO.output(self._pinVerde, GPIO.LOW)
            GPIO.output(self._pinRojo, GPIO.HIGH)
            
    def limpiarLED(self):
        GPIO.cleanup()