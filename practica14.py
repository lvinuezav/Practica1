import requests
import time
from ubidots import ApiClient

api = ApiClient(token='aw3vYXYy13i9xVl75Zt1jQAsQpde8j')
my_variable = api.get_variable('5848c8d47625422c4ec9767e')

response = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=2016-04-01&endtime=2016-04-28")
data = response.text

datos = data.splitlines()

for i in datos:
    j = i.split("|")
    if j[12].find("Ecuador") !=  -1:
        print (j[10])
        new_value = my_variable.save_value({'value': j[10]})
        time.sleep(2)