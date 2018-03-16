#include <Servo.h>

Servo Motor;
int n;

void setup(){
  Serial.begin(9600); //set up serial monitor to be used for reading in
  pinMode(8, OUTPUT); //set up an LED pin
  Motor.attach(13);   //set up a motor
  Motor.write(90);    //make sure the motor is stopped
  n = 0;              //declare n as 0 (basically used as boolean value)
}

void loop(){
  Motor.write(90);    //again make sure motors are stopped
  digitalWrite(8, LOW); //make sure the light is off
  if(Serial.available())  //if the serial monitor is open then read it
    n = Serial.read() - '0';
  if(n==1){               //will read a one from the parent python program
    Motor.write(0);       //turn the motor on
    digitalWrite(8, HIGH);  //turn the LED on
    delay(3000);            //wait three seconds
    n = 0;                  //set n back to 0 so it doesn't enter again
  }
}
