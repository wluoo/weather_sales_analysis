import datetime
from google.cloud import bigquery
from weather_utils import fetch_weather, get_secret, logger, SYDNEY_COORDS, MELBOURNE_COORDS

def write_to_bigquery(table_name, record):
    try:
        # Write to BigQuery
        client = bigquery.Client(project="deft-approach-459711-g2")
        table_id = f"deft-approach-459711-g2.sales_weather_analysis.{table_name}"
        errors = client.insert_rows_json(table_id, [record])
        if errors:
            logger.error(f"BigQuery errors: {errors}")
        else:
            logger.info(f"Data for {record['date']} inserted successfully to {table_name}")
        return "OK"
    except Exception as e:
        logger.error(f"Error writing to BigQuery: {str(e)}")
        raise

if __name__ == "__main__":
    # Get API key from secrets
    API_KEY = get_secret()
    logger.info("Successfully retrieved API key")

    # Get the current date
    current_date = int(datetime.datetime.now().timestamp())

    # Set LAT, LON values for Sydney and Melbourne
    LAT_SYD, LON_SYD = SYDNEY_COORDS
    LAT_MEL, LON_MEL = MELBOURNE_COORDS

    UNITS = 'metric'

    # Get weather values for each location
    weather_syd = fetch_weather(current_date, LAT_SYD, LON_SYD, API_KEY, UNITS)
    weather_mel = fetch_weather(current_date, LAT_MEL, LON_MEL, API_KEY, UNITS)

    # Write data to BigQuery table
    write_to_bigquery("weather_data_syd", weather_syd)
    write_to_bigquery("weather_data_mel", weather_mel)
