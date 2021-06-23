 char EndString[] = "\r\n";
 String Data;
 int runGate = 1;

 //Gate Parameters:
 int GateDurationOpen;
 int GateDurationClosed;
 int timeer = 5000;

void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  Serial.begin(9600); //baudrate
  Serial.setTimeout(5000);

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(1);
  if ((Serial.available()) > 0) {
//    for (int i = 0; i< 3; i++){
//    digitalWrite(13, HIGH);
//    delay(1000);
//    digitalWrite(13, LOW);
//    delay(1000);
//    };
    int timeer = Serial.parseInt(SKIP_ALL, '\r\n');
    Serial.println(timeer);
     //Data = Serial.readStringUntil("=");
     //Serial.println("data");
    digitalWrite(13, HIGH);
    delay(timeer);
    //delay(GateDurationOpen);
    digitalWrite(13, LOW);

//     //if (Data == "G") {
//      runGate = Serial.readStringUntil("\r\n").toInt();
//      digitalWrite(13, HIGH);
//     };
//     
//     if (Data == "OT") {
//      GateDurationOpen = Serial.readStringUntil("/r/n").toInt();
//     };
//     if (Data == "CT") {
//      GateDurationClosed = Serial.readStringUntil("/r/n").toInt();
//     }; 
  };

//  if (runGate == 1) {
//    digitalWrite(13, HIGH);
//    delay(timeer);
//    //delay(GateDurationOpen);
//    digitalWrite(13, LOW);
//    //delay(GateDurationClosed);
//  };
}
