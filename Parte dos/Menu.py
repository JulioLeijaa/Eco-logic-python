from Adafruit import Adafruit
import time

class Menu:
    def __init__(self):
        self.adafruit = Adafruit()

    def haceSubscipciones(self):
        while True:
            self.adafruit.subBomba()
            self.adafruit.subBombaTiempo()
            #time.sleep(1)

main = Menu()
main.haceSubscipciones()