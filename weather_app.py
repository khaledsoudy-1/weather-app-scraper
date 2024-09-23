# A program that REQUESTS current weather from a web service.
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

def get_current_weather():
    print("\n======= Welcome To The Weather-Conditions Page =======")
    
    # Ask user to enter a city name.
    city_name = input("Please, enter a city name: ")

    # Create the request URL using the user's input and API key from environment variables.
    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv("API_KEY")}&units=metric"
    
    # This prints only the request URL, but the weather data is not yet fetched or retrieved.
    print(request_url)
    
get_current_weather()


# NOTE: IF you open this request_url link, it will display the weather data on a web page.
# NOTE: IF you want to fetch (retrieve) weather date ==> use `requests` module.

