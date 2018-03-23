from bs4 import BeautifulSoup
import requests
import serial
import datetime
import time
import os

arduinoSerialData = serial.Serial('/dev/ttyUSB0', 9600)
URL = "0.0.0.0:80"

arduinoSerialData.write('1')
while True:
    Pill1_Hour_List = []
    Pill1_Minute_List = []
    Pill2_Hour_List = []
    Pill2_Minute_List = []
    Pill3_Hour_List = []
    Pill3_Minute_List = []
    # Get the website data from the URL
    r = requests.get("http://0.0.0.0:80")
    
    # Grab and transcribe the raw html using Beautiful Soup
    data = r.content
    page_soup = BeautifulSoup(data, "html.parser")

    # Find and store all the time elements on the webpage
    pill1 = page_soup.findAll("td", {"class":"pill1Time"})
    pill2 = page_soup.findAll("td", {"class":"pill2Time"})
    pill3 = page_soup.findAll("td", {"class":"pill3Time"})

    # Loop through all elements in the list of pill times and store them in lists
    for element in pill1:
        this_time = element.text.split()
        Pill1_Hour_List.append(this_time[0])
        Pill1_Minute_List.append(this_time[2])

    for element in pill2:
        this_time = element.text.split()
        Pill2_Hour_List.append(this_time[0])
        Pill2_Minute_List.append(this_time[2])


    for element in pill3:
        this_time = element.text.split()
        Pill3_Hour_List.append(this_time[0])
        Pill3_Minute_List.append(this_time[2])


    # Update the current time
    now = datetime.datetime.now()
    print(now)
    for x in range(len(Pill1_Hour_List)):
        if now.hour == int(Pill1_Hour_List[x]) and now.minute == int(Pill1_Minute_List[x]):
            arduinoSerialData.write('1')
            print("Dispensing Pill")
	    os.system('omxplayer -o local pillsdispensed.mp3')
    for x in range(len(Pill2_Hour_List)):
        if now.hour == int(Pill2_Hour_List[x]) and now.minute == int(Pill2_Minute_List[x]):
            arduinoSerialData.write('2')
            print("Dispensing Pill")
	    os.system('omxplayer -o local pillsdispensed.mp3')
    for x in range(len(Pill3_Hour_List)):
        if now.hour == int(Pill3_Hour_List[x]) and now.minute == int(Pill3_Minute_List[x]):
            arduinoSerialData.write('3')
            print("Dispensing Pill")
	    os.system('omxplayer -o local pillsdispensed.mp3')
    time.sleep(60)


