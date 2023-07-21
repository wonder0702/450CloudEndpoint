import requests, json
import time
import datetime
i = datetime.datetime.now()
hour = int(i.hour)
hour = hour - 7
yesterdayFlag = 0
if hour < 0:
    yesterdayFlag = 1
    hour = hour + 24
day = int(i.day)
day = day - yesterdayFlag
date = f"{i.year}-0{i.month}-{day}T{hour}:00+00:00"
date = "2023-07-10T22:00+00:00"
key = "28e43f049c2c4a80bcb273f55948a2f9"
p = input("Please enter the location in degrees:\n")
#"121.5,31.25"
#"116.4,39.9"
r = requests.get("https://api.qweather.com/v7/solar-radiation/24h?key="+key+"&location="+p)
l = r.json()["radiation"]
res = None
for i in l:
    if i["fxTime"] == date:
        res = i
finalEnergy = 0.13 * float(res["net"])
print(f"The total Energy is: {finalEnergy} W/m^2")
