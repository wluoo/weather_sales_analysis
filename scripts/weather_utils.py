import requests
import logging
from datetime import datetime
from google.cloud import secretmanager

def fetch_weather(date_obj, lat, lon, api_key, units='metric'):
    """
    Fetch weather data using Weather data for timestamp endpoint
    Args:
        date_obj (int): Unix timestamp in UTC
        lat (float): Latitude
        lon (float): Longitude
        api_key (str): OpenWeatherMap API key
        units (str): Units of measurement (default: 'metric')
    
    Returns:
        dict: Weather data including date, temperature, humidity, wind speed, and description
    """
    url = f"https://api.openweathermap.org/data/3.0/onecall/timemachine"
    params = {
        'lat': lat,
        'lon': lon,
        'dt': date_obj,
        'appid': api_key,
        'units': units
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        logging.info(f"Successfully retrieved weather for timestamp {date_obj}")
        data = response.json()
        weather_data = data['data'][0]  # Get the first (and only) data point
        
        return {
            'date': date_obj,
            'temperature': weather_data.get('temp'),
            'humidity': weather_data.get('humidity'),
            'wind_speed': weather_data.get('wind_speed'),
            'description': weather_data.get('weather', [{}])[0].get('description')
        }
    else:
        logging.error(f"Failed to fetch weather for timestamp {date_obj}: {response.status_code}")
        return {
            'date': date_obj,
            'temperature': None,
            'humidity': None,
            'wind_speed': None,
            'description': None
        }

# Fetch API key securely from Secret Manager
def get_secret(secret_id="openweather-api-key"):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/349833419160/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
MELBOURNE_COORDS = (-37.8136, 144.9631)
SYDNEY_COORDS = (-33.8688, 151.2093) 