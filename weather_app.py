import os
from dotenv import load_dotenv
import requests
from pprint import pprint

# Load environment variables
load_dotenv()


def get_current_weather(city="Cairo"):
    # Create the request URL using the user's input and API key from environment variables
    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=metric"
    
    try:
        # Retrieve and display the weather data
        weather_data = requests.get(request_url).json()
        
        # Check if the request was successful
        if weather_data['cod'] != 200:
            print(f"\n❌  Error: {weather_data['message']}")
        
        return weather_data
    
    
    except requests.RequestException as error:
        print(f"Network error: {error}")
        return None
    
    except ValueError as e:
        print(f"Error: {e}")
        return None


if __name__ == '__main__':
    print("\n======= Welcome To The Weather-Conditions Page =======\n")
    
    # Ask user to enter a city name.
    city_name = input("Please, enter a city name: ")
    
    weather_data = get_current_weather(city_name)
    
    if weather_data is not None:
        # Display more readable data for users.
        print(f"\nCurrent Weather for '{city_name.title()}' City - {weather_data['sys']['country']}:")
        print(f"Temperature : {weather_data['main']['temp']}°C")
        print(f"Feels like  : {weather_data['main']['feels_like']}°C")
        print(f"Weather     : {weather_data['weather'][0]['description'].capitalize()}")



"""
Refactored the weather request logic:
    - Allowing it to be reused as a module for the Flask web application,
    - Enabling separation of concerns between data retrieval and the web interface.
"""
