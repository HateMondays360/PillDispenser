#include <Servo.h>

Servo Motor;
int n;

void setup(){
  Serial.begin(9600);
  pinMode(8, OUTPUT);
  Motor.attach(13);
  Motor.write(90);
  n = 0;
}

void loop(){
  Motor.write(90);
  digitalWrite(8, LOW);
  if(Serial.available())
    n = Serial.read() - '0';
  if(n==1){
    Motor.write(0);
    digitalWrite(8, HIGH);
    delay(3000);
    n = 0;
  }
}
