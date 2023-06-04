#weather.py

import requests
import json

API_KEY = "daf20019452679806146f858c31bab12"  


def weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = json.loads(response.text)
    
    if response.status_code != 200:
        if "message" in data:
            print(f"\t\t\t\tError: {data['message']}")
            cont=input('\t\t\t\tDo you wanna try again? Press 1 to do so,')
            
            if int(cont)==1:
                city = input("\t\t\t\tEnter the name of the city: ")
                weather(city)
            else:
                print("Exiting...")
        else:
            print("\t\t\t\tERROR! ERROR!")
            cont=input('\t\t\t\tDo you wanna try again? Press 1 to do so,')
            
            if int(cont)==1:
                city = input("\t\t\t\tEnter the name of the city: ")
                weather(city)
            else:
                print("\t\t\t\tExiting...")
        return
    
    weather_description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    wind_speed = data["wind"]["speed"]
    temp_max=data["main"]["temp_max"]
    temp_min=data["main"]["temp_min"]
    
    print(f"\n\t\t\t\t\tHello to the people in {city}:)")
    print(f"\t\t\t\tWe can expect {weather_description} in {city} today")
    print(f"\t\t\t\tA temperature of about {temperature}K ")
    print(f"\t\tThe temperature today can reach to a maximun of {temp_max}K or drop to a minimum of {temp_min}K ")
    print(f"\t\t\t\tWind speed of {wind_speed} kts")


if __name__ == "__main__":
    city = input("\n\n\t\t\t\t\tHi! I am Weathery!\n\t\tI can help you get the status of the weather for any city in the world\n\n\n\t\t\t\tPlease enter the name of the city : ")
    weather(city)
