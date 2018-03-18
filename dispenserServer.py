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

Pill1Combined = []
Pill2Combined = []
Pill3Combined = []


def converttomin(minute, hour, combined):
    for x in range(len(hour)):
        hourtominute = int(hour[x])*60
        combined.append(int(minute[x]) + hourtominute)


def sort(arr):
    count = [0]*1441
    for a in arr:
        count[a] += 1
    i = 0
    for a in range(1441):
        for c in range(count[a]):
            arr[i] = a
            i += 1
    return arr


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

    for x in range(len(Pill1Combined)):
        Pill1_Hour_List[x] = int(Pill1Combined[x])
        Pill1_Minute_List[x] = (Pill1Combined[x]-Pill1_Hour_List[x])*(3/5)
    for x in range(len(Pill2Combined)):
        Pill2_Hour_List[x] = int(Pill2Combined[x])
        Pill2_Minute_List[x] = (Pill2Combined[x]-Pill2_Hour_List[x])*(3/5)
    for x in range(len(Pill3Combined)):
        Pill3_Hour_List[x] = int(Pill3Combined[x])
        Pill3_Minute_List[x] = (Pill3Combined[x]-Pill3_Hour_List[x])*(3/5)

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
    
