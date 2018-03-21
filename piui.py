
from flask import Flask, render_template, request
import datetime
import threading
from threading import Thread

app = Flask(__name__)

@app.route('/')
def main():
        return render_template('piui.html')
@app.route('/settings/')
def settings():
        return render_template('settings.html')

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
