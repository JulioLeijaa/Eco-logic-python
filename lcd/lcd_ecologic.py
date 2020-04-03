from lcd.lcddriver import lcd
import time

class lcd_ecologic:
    def __init__(self):
        self.display = lcd()
    
    def imprimirPantalla(self, humedad, temperatura, humedadplantas, ldr, fecha):
        phum = '  Hum. '+str(humedad) +' %'
        ptem = '  Temp. '+str(temperatura)+' C'
        phumplan = ' Humedad '+str(humedadplantas)+' %'
        pldr = ' Sombra  ' +str(ldr)+ ' %'
        dia = fecha[0:11]
        idia = 'Fecha '+fecha
        hora = fecha[12:20]
        ihora = 'Hora  '+hora
        print('Imprimiendo en pantalla')
        self.display.lcd_clear()
        self.display.lcd_display_string(' BIENVENIDOS A', 1)
        self.display.lcd_display_string('   ECO-LOGIC.', 2)
        time.sleep(3)
        self.display.lcd_clear()
        self.display.lcd_display_string(idia, 1)
        self.display.lcd_display_string(ihora, 2)
        time.sleep(3)
        self.display.lcd_clear()
        self.display.lcd_display_string('   CLIMA DE', 1)
        self.display.lcd_display_string('  EL AMBIENTE:', 2)
        time.sleep(3)
        self.display.lcd_clear()
        self.display.lcd_display_string(phum, 1)
        self.display.lcd_display_string(ptem, 2)
        time.sleep(3)
        self.display.lcd_clear()
        self.display.lcd_display_string(' INFORMACION DE', 1)
        self.display.lcd_display_string('  LAS PLANTAS:', 2)
        time.sleep(3)
        self.display.lcd_clear()
        self.display.lcd_display_string(phumplan, 1)
        self.display.lcd_display_string(pldr, 2)
        time.sleep(3)
    
    def limpiarPantalla(self):
        self.display.lcd_clear()
        #except KeyboardInterrupt:
            #print('Pantalla limpiada')
            #self.display.lcd_clear()
        
#pantalla = lcd_ecologic()
#pantalla.imprimirPantalla(35.9, 25.4, 42.6)