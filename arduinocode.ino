#include <Servo.h>

Servo Motor1, Motor2, Motor3;
int n;

void setup(){
  Serial.begin(9600); //set up serial monitor to be used for reading in
  pinMode(8, OUTPUT); //set up an LED pin
  Motor1.attach(13);   //set up a motor
  Motor2.attach(13);   //set up a motor
  Motor3.attach(13);   //set up a motor
  Motor1.write(90);    //make sure the motor is stopped
  Motor2.write(90);    //make sure the motor is stopped
  Motor3.write(90);    //make sure the motor is stopped
  n = 0;              //declare n as 0 (basically used as boolean value)
}

void loop(){
  Motor1.write(90);    //make sure the motor is stopped
  Motor2.write(90);    //make sure the motor is stopped
  Motor3.write(90);    //make sure the motor is stopped
  if(Serial.available())  //if the serial monitor is open then read it
    n = Serial.read() - '0';
  if(n==1){               //will read a one from the parent python program
    Motor1.write(0);       //turn the motor on
    delay(3000);            //wait three seconds
    n = 0;                  //set n back to 0 so it doesn't enter again
  }
  else if(n==2){               //will read a one from the parent python program
    Motor2.write(0);       //turn the motor on
    delay(3000);            //wait three seconds
    n = 0;                  //set n back to 0 so it doesn't enter again
  }
  else if(n==3){               //will read a one from the parent python program
    Motor3.write(0);       //turn the motor on
    delay(3000);            //wait three seconds
    n = 0;                  //set n back to 0 so it doesn't enter again
  }
}
