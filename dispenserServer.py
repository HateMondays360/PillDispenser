from flask import Flask, render_template, request
import serial
import datetime
app = Flask(__name__)

Hour_List = []
Minute_List = []
counter = 0

@app.route("/")
def main():
    templateData = {
        'Hour_List' : Hour_List,
        'Minute_List' : Minute_List
    }
    return render_template('arduinotime.html', **templateData)


@app.route("/", methods = ['POST'])
def addTime():
    hour = request.form['hour']
    minute = request.form['minute']
    Minute_List.append(minute)
    Hour_List.append(hour)
    templateData = {
        'hour' : hour,
        'minute' : minute,
        'Hour_List' : Hour_List,
        'Minute_List' : Minute_List
    }
    
    return render_template('arduinotime.html', **templateData)



def runapp():
    app.run(host = '0.0.0.0', port = 80, debug = True)

if __name__ == '__main__':
    runapp()
    