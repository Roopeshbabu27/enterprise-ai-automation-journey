import requests


def get_coordinates(city):    
    geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=10&language=en&format=json"
    geocode_response = requests.get(geocode_url)
    if geocode_response.status_code == 200:
        data = geocode_response.json()
        if "results" in data:
            latitude = data["results"][0]["latitude"]
            longitude = data["results"][0]["longitude"]
            return {
                "latitude":latitude,
                "longitude":longitude
            }
        else:
            return []
    else:
        print("No records found : ",geocode_response.status_code)

def get_weather(latitude, longitude):
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    weather_response = requests.get(weather_url)
    if weather_response.status_code == 200:
        data = weather_response.json()
        return{
            "temperature" : data["current"]["temperature_2m"],
            "wind_speed" : data["current"]["wind_speed_10m"]
        }        
    else:
        print("No data found for this coordinates: ",weather_response.status_code)     

def display_weather(city,temperature,wind_speed):
    print(
    '''
    Weather Report
    --------------
    '''
    )
    print("City:", city)
    print("Temparature:",temperature)
    print("Wind Speed:",wind_speed)



def main():
    city = input("Enter a city: ")
    location = get_coordinates(city)
    if location:
        weather = get_weather(location["latitude"],location["longitude"])
        temperature = weather["temperature"]
        wind_speed = weather["wind_speed"]
        display_weather(city,temperature,wind_speed)

main()
