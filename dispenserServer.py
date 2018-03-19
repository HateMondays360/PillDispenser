from flask import Flask, render_template, request
import serial
import datetime
app = Flask(__name__)


Pill1_Hour_List = []
Pill1_Minute_List = []
Pill2_Hour_List = []
Pill2_Minute_List = []
Pill3_Hour_List = []
Pill3_Minute_List = []


def converttomin(minute, hour, combined):
    for x in range(len(hour)):
        hourtominute = int(hour[x]) * 60
        combined.append(int(minute[x]) + hourtominute)


def convert_back(combined, hour, minute):
    for x in range(len(combined)):
        temp = combined[x] / 60
        hour[x] = int(temp)
        minute[x] = combined[x] - (hour[x] * 60)


def sort(arr):
    output = [0 for i in range(1441)]
    count = [0 for i in range(1441)]
    for x in arr:
        count[int(x)] += 1
    for a in range(1441):
        count[a] += count[a - 1]
    for i in range(len(arr)):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    for i in range(len(arr)):
        arr[i] = output[i]


@app.route("/")
def main():
    templateData = {
        'Pill1_Hour_List' : Pill1_Hour_List,
        'Pill1_Minute_List' : Pill1_Minute_List,
        'Pill2_Hour_List' : Pill2_Hour_List,
        'Pill2_Minute_List' : Pill2_Minute_List,
        'Pill3_Hour_List' : Pill3_Hour_List,
        'Pill3_Minute_List' : Pill3_Minute_List
    }
    return render_template('arduinotime.html', **templateData)


@app.route("/", methods = ['POST'])
def addTime():
    Pill1Combined = []
    Pill2Combined = []
    Pill3Combined = []
    pillType = request.form['pills']
    print(pillType)
    hour = request.form['hour']
    minute = request.form['minute']
    if pillType == "pill1":
        Pill1_Minute_List.append(minute)
        Pill1_Hour_List.append(hour)
    elif pillType == "pill2":
        Pill2_Minute_List.append(minute)
        Pill2_Hour_List.append(hour)
    elif pillType == "pill3":
        Pill3_Minute_List.append(minute)
        Pill3_Hour_List.append(hour)

    converttomin(Pill1_Minute_List, Pill1_Hour_List, Pill1Combined)
    converttomin(Pill2_Minute_List, Pill2_Hour_List, Pill2Combined)
    converttomin(Pill3_Minute_List, Pill3_Hour_List, Pill3Combined)

    sort(Pill1Combined)
    sort(Pill2Combined)
    sort(Pill3Combined)

    convert_back(Pill1Combined, Pill1_Hour_List, Pill1_Minute_List)
    convert_back(Pill2Combined, Pill2_Hour_List, Pill2_Minute_List)
    convert_back(Pill3Combined, Pill3_Hour_List, Pill3_Minute_List)

    templateData = {
        'Pill1_Hour_List' : Pill1_Hour_List,
        'Pill1_Minute_List' : Pill1_Minute_List,
        'Pill2_Hour_List' : Pill2_Hour_List,
        'Pill2_Minute_List' : Pill2_Minute_List,
        'Pill3_Hour_List' : Pill3_Hour_List,
        'Pill3_Minute_List' : Pill3_Minute_List,
        'pillType' : pillType
    }
    
    return render_template('arduinotime.html', **templateData)


def runapp():
    app.run(host = '0.0.0.0', port = 80, debug = True)


if __name__ == '__main__':
    runapp()

