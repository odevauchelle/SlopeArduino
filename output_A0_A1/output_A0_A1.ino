
int nbMeasurement = 100;
long measurement = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
 
  measurement = 0 ;
  
  for (int i = 0; i < nbMeasurement; i++) {
     measurement += analogRead(A0);
     delay(10);
  }

  Serial.print( measurement );
  Serial.print( ',' );
  Serial.println( nbMeasurement ); 
}
