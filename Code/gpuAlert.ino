void setup() {
	Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(3, OUTPUT);
}
void loop() {
	if(Serial.available() > 0) {
	  int data = Serial.read();
		if (data == 'Y'){
      for (int i = 0; i < 30; i++){
        digitalWrite(LED_BUILTIN, HIGH);  
        digitalWrite(3, HIGH); 
        delay(1000);                       
        digitalWrite(LED_BUILTIN, LOW);   
        digitalWrite(3, LOW);
        delay(1000);  
        if (i == 29){
          break;
        }
      }
    }
	}
}
