DROP TABLE IF EXISTS weather_data;
DROP TABLE IF EXISTS page_titles;

CREATE TABLE weather_data (
    city_name TEXT,
    temp REAL,
    weather_description TEXT
);

CREATE TABLE page_titles (
    title TEXT
);
