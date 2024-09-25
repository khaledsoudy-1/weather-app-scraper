# 🌤️ Weather App

## 📖 Description

Get real-time weather information for any city with this sleek Python-based Weather Conditions App. This project includes both a command-line interface and a web application built with Flask. Simply enter a city name and receive current temperature, "feels like" temperature, and weather description!

## 🌡️ Features

- Real-time weather data from OpenWeatherMap API
- Temperature in Celsius
- "Feels like" temperature
- Current weather description
- Error handling for invalid city names
- Web interface using Flask
- Command-line interface option

## 🚀 How to Use

1. **Set up your environment**:  
   Make sure you have Python installed on your system.
   
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
   - For the web application, execute:
     ```bash
     python main.py
     ```
     Then open a web browser and go to `http://localhost:8000`.
   
   - For the command-line interface, run:
     ```bash
     python weather_app.py
     ```
     Enter the name of a city when prompted to get the current weather.

## 💻 Code Highlights

### Web Application (Flask)
We use Flask to create a web interface for the weather app:

```python
@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    weather_data = get_current_weather(city)
    # ... process and render data
```

### Command-Line Interface
The `weather_app.py` script can be run directly for a CLI experience:

```python
if __name__ == '__main__':
    city_name = input("Please, enter a city name: ")
    weather_data = get_current_weather(city_name)
    # ... display weather information
```

### Production Server
We use Waitress as a production WSGI server:

```python
from waitress import serve

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
```

## 🛠️ Potential Enhancements

- Add support for forecasting weather data.
- Implement caching to reduce API calls for frequently requested cities.
- Add user authentication to allow saving favorite cities.
- Implement a responsive design for better mobile experience.

## 👨‍💻 Author

Khaled Soudy

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📦 Dependencies

This project's dependencies are listed in the `requirements.txt` file. Key dependencies include:

- Flask
- Requests
- Python-dotenv
- Waitress

## 📞 Support

If you encounter any problems or have any questions, please open an issue in the GitHub repository.

---

Stay informed about the weather conditions in any city, anytime! ☀️🌧️❄️
