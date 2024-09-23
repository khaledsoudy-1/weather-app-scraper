# A program that REQUESTS current weather from a web service.
import os
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

def get_current_weather():
    print("\n======= Welcome To The Weather-Conditions Page =======")
    
    # Ask user to enter a city name.
    city_name = input("Please, enter a city name: ")

    # Create the request URL using the user's input and API key from environment variables.
    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv("API_KEY")}&units=metric"
    
    # Retrieve and display the weather data
    weather_data = requests.get(request_url).json()
    
    print(weather_data)
    
get_current_weather()


