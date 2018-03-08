#include <Servo.h>

Servo Motor;

int n;

void setup(){
  Serial.begin(9600);
  Motor.attach(13);
  Motor.write(90);
  n = 0;
}

void loop(){
  Motor.write(90);
  if(Serial.available())
    n = Serial.read() - '0';
  if(n==1){
    Motor.write(0);
    delay(5000);
  }
}
