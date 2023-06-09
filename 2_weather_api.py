# basic weather api that connects to open weather map. org to get up to date weather for acity in engineer
# weather information for any city in the world
# log in to openweathermap.org to generate a api key
# import requests module to go top base url to collect data
# understand a f string

import requests

api_key = "f43ca0a6570520046085384e3e0c723e"
base_url = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter A City Name: ")
request_url = f"{base_url}?appid={api_key}&q={city}"
response = requests.get(request_url)

# check the status code is okay . 200 means okay, if not okay create an error message 

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15,2)
    
    print("Weather:", weather)
    print("Temperature:", temperature, "Celsius")
else:
    print("An Error Occurred")   