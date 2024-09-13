import pandas as pd
from sqlalchemy import create_engine

def store_weather_data(df, db_url):
    if df.empty:
        print("No data to store.")
        return
    engine = create_engine(db_url)
    df.to_sql('weather_data', con=engine, if_exists='append', index=False)
    print(f"DataFrame stored in 'weather_data' table: {df.head()}")

def store_page_title(title, db_url):
    if not title:
        print("No title to store.")
        return
    engine = create_engine(db_url)
    df = pd.DataFrame({'title': [title]})
    df.to_sql('page_titles', con=engine, if_exists='append', index=False)
    print(f"Page title stored in 'page_titles' table: {df.head()}")
