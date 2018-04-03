from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

Pill1_Hour_List = []
Pill1_Minute_List = []
Pill1_Name = ''
Pill1_Num = []
Pill2_Hour_List = []
Pill2_Minute_List = []
Pill2_Name = ''
Pill2_Num = []
Pill3_Hour_List = []
Pill3_Minute_List = []
Pill3_Name = ''
Pill3_Num = []

URL = "0.0.0.0:80"  # Get the website data from the URL
r = requests.get("http://0.0.0.0:80")

# Grab and transcribe the raw html using Beautiful Soup
data = r.content
page_soup = BeautifulSoup(data, "html.parser")

# Find and store all the time elements on the webpage
pill1 = page_soup.findAll("td", {"class": "pill1Time"})
pill2 = page_soup.findAll("td", {"class": "pill2Time"})
pill3 = page_soup.findAll("td", {"class": "pill3Time"})
numpill1 = page_soup.findAll("td", {"class": "pill1num"})
numpill2 = page_soup.findAll("td", {"class": "pill2num"})
numpill3 = page_soup.findAll("td", {"class": "pill3num"})

# Loop through all elements in the list of pill times and store them in lists
for x in range(len(pill1)):
    Pill1_Num.append(int(numpill1[x].text))
    this_time = pill1[x].text.split()
    Pill1_Hour_List.append(this_time[0])
    Pill1_Minute_List.append(this_time[2])

for x in range(len(pill2)):
    Pill2_Num.append(int(numpill2[x].text))
    this_time = pill2[x].text.split()
    Pill2_Hour_List.append(this_time[0])
    Pill2_Minute_List.append(this_time[2])

for x in range(len(pill3)):
    Pill3_Num.append(int(numpill3[x].text))
    this_time = pill3[x].text.split()
    Pill3_Hour_List.append(this_time[0])
    Pill3_Minute_List.append(this_time[2])


@app.route("/")
def main():
    templateData = {
        'Pill1_Hour_List': Pill1_Hour_List,
        'Pill1_Minute_List': Pill1_Minute_List,
        'Pill1_Name': Pill1_Name,
        'Pill1_Num': Pill1_Num,

        'Pill2_Hour_List': Pill2_Hour_List,
        'Pill2_Minute_List': Pill2_Minute_List,
        'Pill2_Name': Pill2_Name,
        'Pill2_Num': Pill2_Num,

        'Pill3_Hour_List': Pill3_Hour_List,
        'Pill3_Minute_List': Pill3_Minute_List,
        'Pill3_Name': Pill3_Name,
        'Pill3_Num': Pill3_Num
    }
    return render_template('clientview.html', **templateData)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
