import time
from Adafruit_IO import MQTTClient

class Adafruit:
    def __init__(self):
        ADAFRUIT_IO_KEY = '05037193ee4a460eb2e5ba8bc1e91a45'
        ADAFRUIT_IO_USERNAME = 'Cesar_utt'
        self.client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
        self.client.connect()
        self.client.loop_background()
    
    def connected(self):
        print('Conectado a Adafruit IO!')
    
    def publicarHumedad(self, humedad):
        print('Publicando {0} en Humedad.'.format(humedad))
        self.client.publish('Humedad', humedad)
        
    def publicarTemperatura(self, temperatura):
        print('Publicando {0} en Temperatura.'.format(temperatura))
        self.client.publish('Temperatura', temperatura)
        
    def publicarHumedadPlanta(self, humedadplanta):
        print('Publicando {0} en Humedadplanta.'.format(humedadplanta))
        self.client.publish('Humedadplantas', humedadplanta)
        
    def publicarLDR(self, ldr):
        print('Publicando {0} en LDR.'.format(ldr))
        self.client.publish('LDR', ldr)