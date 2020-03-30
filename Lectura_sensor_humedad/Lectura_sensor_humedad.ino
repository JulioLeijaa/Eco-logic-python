int prom;    //https://www.instructables.com/id/Raspberry-Pi-Arduino-Serial-Communication/
int lectura;

void setup() {
Serial.begin(9600);              //Starting serial communication
}

void haceLectura(){
  for (int i= 0; i < 5; i++){
    lectura = analogRead(A0);
    //Serial.println(lectura);
    prom += lectura;
    }
  prom = prom / 5;
  //Serial.print("El promedio es: ");
  Serial.println(prom);
  prom = 0;
}

void loop() {
  haceLectura();
  delay(1000);                  // give the loop some break
}
