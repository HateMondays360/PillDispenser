#include <Servo.h>

Servo Motor1, Motor2, Motor3, Water;
bool water;
void setup() {
  Serial.begin(9600); //set up serial monitor to be used for reading in
  Motor1.attach(9);   //set up a motor
  Motor2.attach(10);   //set up a motor
  Motor3.attach(11);   //set up a motor
  Water.attach(12);
  Motor1.write(90);    //make sure the motor is stopped
  Motor2.write(90);    //make sure the motor is stopped
  Motor3.write(90);    //make sure the motor is stopped
  Water.write(0);
}

void loop() {
  water = false;
  int num = 0, num1 = 0, num2 = 0, one = 0, two = 0, three = 0, n = 0, n1 = 0, n2 = 0;
  String value = "";
  Motor1.write(90);    //make sure the motor is stopped
  Motor2.write(90);    //make sure the motor is stopped
  Motor3.write(90);    //make sure the motor is stopped
  if (Serial.available()) { //if the serial monitor is open then read it
    value = "";
    value = Serial.readString();
    if (value.length() == 2) {
      n = value.toInt() / 10;
      num = value.toInt() % 10;
    }
    else if (value.length() == 4) {
      one = value.substring(0, 2).toInt();
      n = one / 10;
      num = one % 10;
      two = value.substring(2).toInt();
      n1 = two / 10;
      num1 = two % 10;
    }
    else if (value.length() == 6) {
      one = value.substring(0, 2).toInt();
      n = one / 10;
      num = one % 10;
      two = value.substring(2, 4).toInt();
      n1 = two / 10;
      num1 = two % 10;
      three = value.substring(4).toInt();
      n2 = three / 10;
      num2 = three % 10;
    }
  }
  if (n == 1) {           //will read a one from the parent python program
    Motor1.write(0);       //turn the motor on
    delay(1300 * num);          //wait three seconds
    Motor1.write(90);
    n = 0;                  //set n back to 0 so it doesn't enter again
    num = 0;
    water = true;
  }
  if (n == 2) {           //will read a one from the parent python program
    Motor2.write(0);       //turn the motor on
    delay(1300 * num);          //wait three seconds
    Motor2.write(90);
    n = 0;                  //set n back to 0 so it doesn't enter again
    num = 0;
    water = true;
  }
  else if (n1 == 2) {
    Motor2.write(0);
    delay(1300 * num1);
    Motor2.write(90);
    n1 = 0;
    num1 = 0;
    water = true;
  }
  if (n == 3) {           //will read a one from the parent python program
    Motor3.write(0);       //turn the motor on
    delay(1300 * num);          //wait three seconds
    Motor3.write(90);
    n = 0;                  //set n back to 0 so it doesn't enter again
    num = 0;
    water = true;
  }
  else if (n1 == 3) {
    Motor3.write(0);
    delay(1300 * num1);
    Motor3.write(90);
    n1 = 0;
    num1 = 0;
    water = true;
  }
  else if (n2 == 3) {           //will read a one from the parent python program
    Motor3.write(0);       //turn the motor on
    delay(1300 * num2);          //wait three seconds
    Motor3.write(90);
    n2 = 0;                  //set n back to 0 so it doesn't enter again
    num2 = 0;
    water = true;
  }
  if (water) {
    Water.write(90);
    delay(6000);
    water = false;
  }
}
