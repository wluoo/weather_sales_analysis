import pandas as pd
from datetime import datetime
from weather_utils import fetch_weather, get_secret, logger, MELBOURNE_COORDS

# --- CONFIG ---
INPUT_FILE = 'data/ProductsbyDate.csv'
OUTPUT_FILE = 'data/weather_data_mel.csv'
LAT, LON = MELBOURNE_COORDS
UNITS = 'metric'

# --- LOAD CSV AND GET UNIQUE DATES ---
def get_unique_dates():
    df = pd.read_csv(INPUT_FILE)
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')  # First convert to datetime
    unique_dates = df['Order Date'].dt.strftime('%Y-%m-%d').unique()  # Convert to YYYY-MM-DD string format

    # print(unique_dates)
    print(f"Found {len(unique_dates)} unique dates.")
    return unique_dates

# --- LOOP AND FETCH ---
def fetch_weather_records(unique_dates, api_key):
    weather_records = []
    for date in unique_dates:
        weather = fetch_weather(date, LAT, LON, api_key, UNITS)
        weather_records.append(weather)
    return weather_records

# --- CREATE DATAFRAME AND EXPORT ---
def create_weather_csv(weather_records):
    weather_df = pd.DataFrame(weather_records)
    # Convert the date column back to DD/MM/YYYY format before saving
    weather_df['date'] = pd.to_datetime(weather_df['date']).dt.strftime('%d/%m/%Y')
    weather_df.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved weather data to {OUTPUT_FILE}")

if __name__ == "__main__":
    API_KEY = get_secret()
    logger.info("Successfully retrieved API key")

    # Extract unique dates and store in dataframe
    unique_dates_df = get_unique_dates()

    # Get weather data for each date
    weather_records = fetch_weather_records(unique_dates_df, API_KEY)

    # Create csv file with weather data
    create_weather_csv(weather_records)

