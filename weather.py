f = open("weather.txt","a")
f.write("\nWEATHER STATS FOR:")
import requests
from datetime import datetime
api_key = '4f0db74f7b69d1829f223be4849b19d2'
location = input("ENTER CITY NAME: ")
f.write(location + "\n")
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
f.write("Current temperature: " + str(temp_city) + "deg C" + "\n")
f.write("Current weather description: " + str(weather_desc) + "\n")
f.write("Current humidity: " + str(hmdt) + "%" + "\n")
f.write("Current wind speed: " + str(temp_city) + "kmph" + "\n")
print("------------------------------------------------------")
print("WEATHER STATS FOR- {} || {}".format(location.upper(), date_time))
print("------------------------------------------------------")
print("Current temperature is:{:2f}deg C".format(temp_city))
print("Current weather description:",weather_desc)
print("Current humidity:",hmdt,"%")
print("Current wind speed:",wind_spd,"kmph")
f.close()
