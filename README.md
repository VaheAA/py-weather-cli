# py-weather-cli

A simple command-line weather application that fetches current weather data for your location or any city worldwide.

## Features

- 🌍 Get weather for your current location (based on IP)
- 🏙️ Search weather for any city globally
- 🌡️ Display temperature, humidity, wind speed, and weather conditions
- 💻 Interactive CLI with arrow-key navigation

## Prerequisites

- Python 3.7+
- OpenWeather API key (free tier available at [OpenWeatherMap](https://openweathermap.org/api))

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/py-weather-cli.git
cd py-weather-cli
```

2. Install required dependencies:

```bash
pip install requests geocoder python-dotenv inquirer
```

3. Create a `.env` file in the project root:

```bash
OPEN_WEATHER_API_KEY=your_api_key_here
OPEN_WEATHER_API_URL=https://api.openweathermap.org/data/3.0/onecall
GITHUB_USER_NAME=yourusername
```

## Usage

Run the application:

```bash
python src/main.py
```

You'll be prompted to choose between:

- **My location**: Automatically detects your location based on IP
- **Custom location**: Enter any city name to get its weather

## Example Output

```
Location: New York, United States
Current weather: clear sky
Temperature: 22.5°C
Humidity: 65%
Wind speed: 3.2 m/s
```

## Project Structure

```
py-weather-cli/
├── src/
│   ├── main.py                 # Main application entry point
│   └── modules/
│       ├── cli_select.py        # CLI interface and user input
│       ├── geocoder.py          # Location and weather API handling
│       └── settings/
│           └── settings.py      # Environment configuration
├── .env                         # Environment variables (create this)
├── .gitignore
└── README.md
```

## API Services

- **OpenWeather API**: Provides weather data
- **OpenStreetMap Nominatim**: Geocoding for custom locations
- **IP Geocoding**: Automatic location detection

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

This project is open source and available under the MIT License.
