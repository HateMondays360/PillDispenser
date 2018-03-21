from flask import Flask, render_template, request
import serial
import datetime
app = Flask(__name__)


Pill1_Hour_List = []
Pill1_Minute_List = []
Pill1_Name=''
Pill1_Num=0
Pill2_Hour_List = []
Pill2_Minute_List = []
Pill2_Name=''
Pill2_Num=0
Pill3_Hour_List = []
Pill3_Minute_List = []
Pill3_Name=''
Pill3_Num=0

@app.route("/")
def main():
    templateData = {
        'Pill1_Hour_List' : Pill1_Hour_List,
        'Pill1_Minute_List' : Pill1_Minute_List,
        'Pill1_Name' : Pill1_Name,
        'Pill1)_Num' : Pill1_Num,

        'Pill2_Hour_List' : Pill2_Hour_List,
        'Pill2_Minute_List' : Pill2_Minute_List,
        'Pill2_Name' : Pill2_Name,
        'Pill2_Num' : Pill2_Num,

        'Pill3_Hour_List' : Pill3_Hour_List,
        'Pill3_Minute_List' : Pill3_Minute_List,
        'Pill3_Name' : Pill3_Name,
        'Pill3_Num' : Pill3_Num

    }
    return render_template('arduinotime.html', **templateData)


@app.route("/", methods = ['POST'])
def addTime():

    global Pill1_Name
    global Pill2_Name
    global Pill3_Name
    global Pill1_Num
    global Pill2_Num
    global Pill3_Num

    pillType = request.form['pills']
    numPills= request.form['Select # of Pills to be dispensed']

    print(pillType)
    hour = request.form['hour']
    minute = request.form['minute']
    name=request.form['name']

    if pillType == "pill1":
        Pill1_Name=name
        Pill1_Minute_List.append(minute)
        Pill1_Hour_List.append(hour)
        Pill1_Num=numPills

    elif pillType == "pill2":
        Pill2_Name=name
        Pill2_Minute_List.append(minute)
        Pill2_Hour_List.append(hour)
        Pill1_Num=numPills


    elif pillType == "pill3":
        Pill3_Name=name
        Pill3_Minute_List.append(minute)
        Pill3_Hour_List.append(hour)
        Pill1_Num=numPills


    templateData = {
        'Pill1_Hour_List' : Pill1_Hour_List,
        'Pill1_Minute_List' : Pill1_Minute_List,
        'Pill1_Name' : Pill1_Name,
        'Pill1_Num' : Pill1_Num,

        'Pill2_Hour_List' : Pill2_Hour_List,
        'Pill2_Minute_List' : Pill2_Minute_List,
        'Pill2_Name' : Pill2_Name,
        'Pill2_Num' : Pill2_Num,

        'Pill3_Hour_List' : Pill3_Hour_List,
        'Pill3_Minute_List' : Pill3_Minute_List,
        'Pill3_Name' : Pill3_Name,
        'Pill3_Num' : Pill3_Num,

        'pillType' : pillType
    }

    return render_template('arduinotime.html', **templateData)



def runapp():
    app.run(debug=True, host = '0.0.0.0')

if __name__ == '__main__':
    runapp()
