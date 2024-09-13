from dotenv import load_dotenv
import os
from src.data_extraction import fetch_page_title, fetch_weather_data
from src.data_processing import clean_weather_data, clean_page_title
from src.data_storage import store_weather_data, store_page_title
from database.db_config import DB_URL
from db_utils import create_tables


load_dotenv()

def main():
    create_tables(DB_URL)
    
    api_key = os.getenv('API_KEY')
    city = 'London'
    
    weather_data = fetch_weather_data(api_key, city)
    if weather_data:
        cleaned_weather_data = clean_weather_data([weather_data])
        store_weather_data(cleaned_weather_data, DB_URL)
    
    page_url = 'https://en.wikipedia.org/wiki/Data_science'
    page_title = fetch_page_title(page_url)
    cleaned_page_title = clean_page_title(page_title)
    store_page_title(cleaned_page_title, DB_URL)

if __name__ == "__main__":
    main()
