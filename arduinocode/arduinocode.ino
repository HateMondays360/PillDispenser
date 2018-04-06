#include <Adafruit_TiCoServo.h>
#include <known_16bit_timers.h>

Adafruit_TiCoServo Motor1, Motor2, Motor3, Water;
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 8
bool water;
Adafruit_NeoPixel strip = Adafruit_NeoPixel(60, PIN, NEO_GRB + NEO_KHZ800);
void setup(){
// This is for Trinket 5V 16MHz, you can remove these three lines if you are not using a Trinket
  #if defined (__AVR_ATtiny85__)
    if (F_CPU == 16000000) clock_prescale_set(clock_div_1);
  #endif
  // End of trinket special code
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
  Serial.begin(9600); //set up serial monitor to be used for reading in
  Motor1.attach(13);   //set up a motor
  Motor2.attach(12);   //set up a motor
  Motor3.attach(11);   //set up a motor
  Water.attach(9);
  Motor1.write(90);    //make sure the motor is stopped
  Motor2.write(90);    //make sure the motor is stopped
  Motor3.write(90);    //make sure the motor is stopped
  Water.write(0);
  strip.setBrightness(64);
}

void loop(){
  water = false;
  Water.write(0);
  rainbowCycle(50);
  int num=0, num1=0, num2=0, one=0, two=0, three=0, n=0, n1=0, n2=0;
  String value = "";
  Motor1.write(90);    //make sure the motor is stopped
  Motor2.write(90);    //make sure the motor is stopped
  Motor3.write(90);    //make sure the motor is stopped
  if(Serial.available()){  //if the serial monitor is open then read it
    value = Serial.readString();
    if(value.length()==2){
      n = value.toInt()/10;
      num = value.toInt()%10;
    }
    else if(value.length()==4){
      one = value.substring(0, 2).toInt();
      n = one/10;
      num = one%10;
      two = value.substring(2).toInt();
      n1 = two/10;
      num1 = two%10;
    }
    else if(value.length()==6){
      one = value.substring(0, 2).toInt();
      n = one/10;
      num = one%10;
      two = value.substring(2, 4).toInt();
      n1 = two/10;
      num1 = two%10;
      three = value.substring(4).toInt();
      n2 = three/10;
      num2 = three%10;
    }
  }
  if(n==1){               //will read a one from the parent python program
    Motor1.write(0);       //turn the motor on
    delay(2600*num);            //wait three seconds
    Motor1.write(90);
    n = 0;                  //set n back to 0 so it doesn't enter again
    num = 0;
    water = true;
  }
  if(n==2){               //will read a one from the parent python program
    Motor2.write(0);       //turn the motor on
    delay(2600*num);            //wait three seconds
    Motor2.write(90);
    n = 0;                  //set n back to 0 so it doesn't enter again
    num = 0;
    water = true;
  }
  else if(n1==2){
    Motor2.write(0);
    delay(2600*num1);
    Motor2.write(90);
    n1 = 0;
    num1 = 0;
    water = true;
  }
  if(n==3){               //will read a one from the parent python program
    Motor3.write(0);       //turn the motor on
    delay(2600*num);            //wait three seconds
    Motor3.write(90);
    n = 0;                  //set n back to 0 so it doesn't enter again
    num = 0;
  }
  else if(n1==3){
    Motor3.write(0);
    delay(2600*num1);
    Motor3.write(90);
    n1 = 0;
    num1 = 0;
    water = true;
  }
  else if(n2==3){               //will read a one from the parent python program
    Motor3.write(0);       //turn the motor on
    delay(2600*num2);            //wait three seconds
    Motor3.write(90);
    n2 = 0;                  //set n back to 0 so it doesn't enter again
    num2 = 0;
    water = true;
  }
  if(water){
    Water.write(90);
    delay(4000);
    water = false;
  }
}

void rainbowCycle(uint8_t wait) {
  uint16_t i, j;
  
  for(j=0; j<256*5; j++) { // 5 cycles of all colors on wheel
    for(i=0; i< strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

uint32_t Wheel(byte WheelPos) {
  WheelPos = 255 - WheelPos;
  if(WheelPos < 85) {
    return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  }
  if(WheelPos < 170) {
    WheelPos -= 85;
    return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
  WheelPos -= 170;
  return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
}
