# PillDispenser

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/V9uTrwy9Qtg/0.jpg)](https://www.youtube.com/watch?v=V9uTrwy9Qtg)

This project was completed as part of a Cornerstone of Engineering project at Northeastern University.
Participating members were Matthew Swenson, Oscar Chen, and myself.

We were tasked with creating a robotic device that met a need. To this we crafted an automatic pill dispenser.
The pill dispenser hosts a webpage that the doctor or caretaker can access and input three different pills, how many need to be dispensed, and when they will be dispensed. This data is then displayed on a small screen on the device so the patient can view when their pills are. An added feature is the dispensing of water with the pills to remove all excuses of not taking pills. The compartment containg the pills is also locked to prevent the abuse of pills.

Additionally, an Alexa Skill was created where the user can ask when the pills will be dispensed and Alexa will respond accordingly. 

Physical Components used were:
  3 Continuous rotation Servos,
  1 180 degree Servo,
  A Neopixel Light Strip,
  Sparkfun Redboard,
  Protoboard,
  Arduino Micro,
  Raspberry Pi 3,
  2.8" GPIO Controlled Touch Scrren for the Raspberry Pi,
  Water Balloon Valve,
  Wood,
  Hotglue,
  Stain (Dark Chestnut),
  Velcro,
  Acrylic Strips,
  Wire,
  
In terms of Software...
  All the above code was used and implemented onto the Raspberry Pi. A tunneling service known as pagekite was used to host both the doctor   end of the dispenserServer.py and the AlexaSkill.py. Additional libraries include datetime, time, serial, flask, flask-ask, requests, and   Beautiful Soup.
