# A program that REQUESTS current weather from a web service.
import os
from dotenv import load_dotenv
import requests
from pprint import pprint

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
    
    pprint(weather_data)
    
    # Display more readable data for users.
    print(f"\nCurrent Weather for '{city_name.title()}' City - {weather_data['sys']['country']}:")
    print(f"Temperature : {weather_data['main']['temp']}°C")
    print(f"Feels like  : {weather_data['main']['feels_like']}°C")
    print(f"Weather     : {weather_data['weather'][0]['description'].capitalize()}")

    
if __name__ == '__main__':
    get_current_weather()


# NOTE: The Code for successful request ==> 'cod': 200
# NOTE: Which means that any other code will refer to an error along with an error message
# NOTE: For Example: If you pass any wrong city name.
