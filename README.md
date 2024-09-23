
# 🌤️ Weather App

## 📖 Description

Get real-time weather information for any city with this sleek Python-based Weather Conditions App. Simply enter a city name and receive current temperature, "feels like" temperature, and weather description!

## 🌡️ Features

- Real-time weather data from OpenWeatherMap API
- Temperature in Celsius
- "Feels like" temperature
- Current weather description
- Error handling for invalid city names

## 🚀 How to Use

1. **Set up your environment**:  
   Make sure you have Python installed on your system and the required packages installed. The `requirements.txt` file includes the necessary libraries.
   
2. **Obtain an API Key**:  
   Sign up on [OpenWeather](https://openweathermap.org/) and get your free API key.

3. **Set up your environment variables**:  
   Create a `.env` file in the project directory and add your API key like this:
   ```plaintext
   API_KEY=your_openweather_api_key
   ```

4. **Install dependencies**:  
   Run the following command to install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the App**:  
   Execute the app using the following command:
   ```bash
   python weather_app.py
   ```
   Enter the name of a city when prompted to get the current weather.

## 💻 Code Highlights

### Environment Variables
We use `python-dotenv` to securely load API keys:

```python
from dotenv import load_dotenv

load_dotenv()
```

### API Request
We use the `requests` library to fetch real-time weather data from the OpenWeather API:
```python
weather_data = requests.get(request_url).json()
```
The data is then parsed and displayed in a readable format for users.

## 🛠️ Potential Enhancements

- Add support for forecasting weather data.
- Implement error handling for different API failure scenarios.
- Build a graphical interface for a more interactive experience.

## 👨‍💻 Author

Khaled Soudy

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📦 Dependencies

This project's dependencies are listed in the `requirements.txt` file. You can install them using pip as described in the "How to Use" section.


## 📞 Support

If you encounter any problems or have any questions, please open an issue in the GitHub repository.

---

Stay informed about the weather conditions in any city, anytime! ☀️🌧️❄️