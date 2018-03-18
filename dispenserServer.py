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
    
