int prom_hum;
int lectura_hum;
int prom_ldr;
int lectura_ldr;

void setup() {
  Serial.begin(9600);
}

void lecturaHum(){
  for (int i= 0; i < 5; i++){
    lectura_hum = analogRead(A0);
    //Serial.println(lectura);
    prom_hum += lectura_hum;
    }
  prom_hum = prom_hum / 5;
  //Serial.print("El promedio es: ");
  //Serial.println(prom_hum);
}

void lecturaLDR(){
  for (int i= 0; i < 5; i++){
    lectura_ldr = analogRead(A4);
    //Serial.println(lectura);
    prom_ldr += lectura_ldr;
    }
  prom_ldr = prom_ldr / 5;
  //Serial.print("El promedio es: ");
  //Serial.println(prom_hum);
}
void loop() {
 lecturaHum();
 lecturaLDR();
 Serial.println("{\"hum\":\"" + String(prom_hum) +
                "\", \"ldr\":\"" + String(prom_ldr) +
                "\"}");
  prom_hum = 0;
  prom_ldr = 0;
  delay(2000);
}
