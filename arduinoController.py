from bs4 import BeautifulSoup
import requests
import serial
import datetime
import time

arduinoSerialData = serial.Serial('/dev/ttyUSB0', 9600)
URL = "0.0.0.0:80"

arduinoSerialData.write('1')
while True:
    Hour_List = []
    Minute_List = []
    # Get the website data from the URL
    r = requests.get("http://10.60.157.218")
    
    # Grab and transcribe the raw html using Beautiful Soup
    data = r.content
    page_soup = BeautifulSoup(data, "html.parser")

    # Find and store all the time elements on the webpage
    table = page_soup.findAll("td", {"class":"pillTime"})

    # Loop through all elements in the list of pill times and store them in lists
    for time in table:
        this_time = time.text.split()
        Hour_List.append(this_time[0])
        Minute_List.append(this_time[2])

    # Update the current time
    now = datetime.datetime.now()
    print(now)
    for x in range(len(Hour_List)):
        if now.hour == int(Hour_List[x]) and now.minute == int(Minute_List[x]) and now.second == 0:
            arduinoSerialData.write('1')
            print("yayyyyy")
	    continue
    # time.sleep(5)
