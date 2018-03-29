from flask import Flask
from flask_ask import Ask, statement, convert_errors
import logging
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
ask = Ask(app, '/')

first = True

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


def string_from_lists(HourList, MinuteList, am_or_pm, pill_name):
    global first
    pills = ''
    for x in range(len(HourList)):
        if HourList[x] > 12:
            HourList[x] %= 12
            am_or_pm.append(' PM ')
        else:
            am_or_pm.append(' AM ')
        if first:
            pills = str(HourList[x]) + ' ' + str(MinuteList[x]) + am_or_pm[x]
            first = False
        else:
            pills += ' and ' + str(HourList[x]) + ' ' + str(MinuteList[x]) + am_or_pm[x]
    return pill_name + ' at ' + pills


@ask.intent('GPIOControlIntent', mapping={})
def gpio_control():
    global first
    first = False
    pills = ''
    Pill1_Hour_List = []
    Pill1_Minute_List = []
    Pill2_Hour_List = []
    Pill2_Minute_List = []
    Pill3_Hour_List = []
    Pill3_Minute_List = []
    am_or_pm = []

    r = requests.get("http://0.0.0.0:80")
    data = r.content
    page_soup = BeautifulSoup(data, "html.parser")
    try:
        pill1 = page_soup.findAll("td", {"class": "pill1Time"})
        pill2 = page_soup.findAll("td", {"class": "pill2Time"})
        pill3 = page_soup.findAll("td", {"class": "pill3Time"})
        pill1name = page_soup.find("p", {"id": "pill1name"}).text
        pill2name = page_soup.find("p", {"id": "pill2name"}).text
        pill3name = page_soup.find("p", {"id": "pill3name"}).text

        # Loop through all elements in the list of pill times and store them in lists
        for element in pill1:
            this_time = element.text.split()
            Pill1_Hour_List.append(int(this_time[0]))
            Pill1_Minute_List.append(int(this_time[2]))

        for element in pill2:
            this_time = element.text.split()
            Pill2_Hour_List.append(int(this_time[0]))
            Pill2_Minute_List.append(int(this_time[2]))

        for element in pill3:
            this_time = element.text.split()
            Pill3_Hour_List.append(int(this_time[0]))
            Pill3_Minute_List.append(int(this_time[2]))

        if len(Pill1_Hour_List) > 0:
            pills += string_from_lists(Pill1_Hour_List, Pill1_Minute_List, am_or_pm, pill1name)
        if len(Pill2_Hour_List) > 0:
            pills += string_from_lists(Pill2_Hour_List, Pill2_Minute_List, am_or_pm, pill2name)
        if len(Pill3_Hour_List) > 0:
            pills += string_from_lists(Pill3_Hour_List, Pill3_Minute_List, am_or_pm, pill3name)
        return statement('You have {}'.format(pills))
    except Exception as e:
        return 'it did not work'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
