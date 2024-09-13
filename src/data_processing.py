import pandas as pd

def clean_weather_data(data_list):
    if not data_list:
        print("No data to process.")
        return pd.DataFrame()

    df_list = []
    for data in data_list:
        df = pd.json_normalize(data, sep='_')

        # Debug prints
        print(f"Raw DataFrame: {df.head()}")

        if isinstance(data.get('weather'), list) and len(data['weather']) > 0:
            df['weather_description'] = data['weather'][0].get('description', '')
        else:
            df['weather_description'] = 'No description available'

        df.rename(columns={
            'name': 'city_name',
            'main_temp': 'temp'
        }, inplace=True)

        required_columns = ['city_name', 'temp', 'weather_description']
        for col in required_columns:
            if col not in df.columns:
                print(f"Warning: '{col}' column is missing.")

        try:
            df = df[required_columns]
        except KeyError as e:
            print(f"KeyError: {e}. Check the columns in the DataFrame.")

        df_list.append(df)

    if not df_list:
        print("No DataFrames to concatenate.")
        return pd.DataFrame()

    final_df = pd.concat(df_list, ignore_index=True)
    print(f"Cleaned DataFrame: {final_df.head()}")  # Debug print
    return final_df





def clean_page_title(title):
    cleaned_title = title.strip().replace('  ', ' ')
    
    return cleaned_title