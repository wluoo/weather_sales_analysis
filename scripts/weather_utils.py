import requests
import logging
from datetime import datetime
from google.cloud import secretmanager

def fetch_weather(date_obj, lat, lon, api_key, units='metric'):
    """
    Fetch weather data for a specific date and location.
    
    Args:
        date_obj (str): Date in YYYY-MM-DD format
        lat (float): Latitude
        lon (float): Longitude
        api_key (str): OpenWeatherMap API key
        units (str): Units of measurement (default: 'metric')
    
    Returns:
        dict: Weather data including date, temperature, humidity, and wind speed
    """
    url = f"https://api.openweathermap.org/data/3.0/onecall/day_summary"
    params = {
        'lat': lat,
        'lon': lon,
        'date': date_obj,
        'appid': api_key,
        'units': units
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        logging.info(f"Successfully retrieved weather for {date_obj}")
        data = response.json()
        return {
            'date': date_obj,
            'temperature': data.get('temperature').get('max'),
            'humidity': data.get('humidity').get('afternoon'),
            'wind_speed': data.get('wind').get('max').get('speed'),
        }
    else:
        logging.error(f"Failed to fetch weather for {date_obj}: {response.status_code}")
        return {
            'date': date_obj,
            'temperature': None,
            'humidity': None,
            'wind_speed': None
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