from Adafruit import Adafruit
import time

class Menu:
    def __init__(self):
        self.adafruit = Adafruit()

    def run(self):
        try:
            while True:
                self.adafruit.subBomba()
                self.adafruit.subBombaTiempo()
        except KeyboardInterrupt:
            print('Ejecución detenida')