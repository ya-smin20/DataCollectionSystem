import json
import requests
from bs4 import BeautifulSoup


def fetch_weather_data(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    print(f"Fetching data from URL: {url}")  
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=2))  
        return data
    else:
        print(f"Failed to fetch data for city {city}: {response.status_code}")
        return None




def fetch_page_title(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title_tag = soup.find('title')
        
        if title_tag:
            return title_tag.text
        else:
            print("Page title not found.")
            return None
    else:
        print(f"Failed to fetch page: {response.status_code}")
        return None
