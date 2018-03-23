from flask import Flask
from flask_ask import Ask, statement, convert_errors
import logging
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.intent('GPIOControlIntent', mapping={})
def gpio_control():
    pills = ''
    Pill1_Hour_List = []
    Pill1_Minute_List = []
    Pill2_Hour_List = []
    Pill2_Minute_List = []
    Pill3_Hour_List = []
    Pill3_Minute_List = []
    pill1name = ''
    try:
        r = requests.get("http://10.60.157.218")
        data = r.content
        page_soup = BeautifulSoup(data, "html.parser")

        pill1 = page_soup.findAll("td", {"class": "pill1Time"})
        pill2 = page_soup.findAll("td", {"class": "pill2Time"})
        pill3 = page_soup.findAll("td", {"class": "pill3Time"})
        pill1name = page_soup.find("p", {"id": "pill1name"}).text

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

    except Exception as e:
        return statement('You have no pills.')

    for x in range(len(Pill1_Hour_List)):
        Pill1_Hour_List[x] %= 12
        pills += 'and' + str(Pill1_Hour_List[x]) + str(Pill1_Minute_List[x])
    return statement('You have {} at {}'.format(pill1name, pills))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
