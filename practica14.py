import requests

response = requests.get("http://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=2016-04-01&endtime=2016-04-28")
data = response.text

datos = data.splitlines()

for i in datos:
    j = i.split("|")
    if j[12].find("Ecuador") !=  -1:
        print (j[10])