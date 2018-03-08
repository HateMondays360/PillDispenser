import serial
import datetime

one = input('Enter the first time: ')
two = input('Enter the second time: ')
arduinoSerialData = serial.Serial('/dev/ttyUSB0', 9600)
now = datetime.datetime.now()
while now.time < datetime.time(hour = 2, minute = one):   # the pi's time when i was working on it was set to 2:00
  now = datetime.datetime.now()
arduinoSerialData.write('1')
while now.time() < datetime.time(hour = 2, minute = two):
  now = datetime.datetime.now()
arduinoSerialData.write('1')
