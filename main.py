import requests
from datetime import datetime

my_lat = Your_lat
my_long = Your_long

parameters = {"lat":my_lat,"lng":my_long, "formatted" : 0}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

now = datetime.now()

print(now.hour)
