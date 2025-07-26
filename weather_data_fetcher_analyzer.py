#Weather Data Fetcher & Analyzer

import requests
import csv
import os

def fetch_weather(city:str,api_key:str):  #defines the function
  "Fetching weather data for a given city using OpenWeatherMap API"
  url = "https://api.openweathermap.org/data/2.5/weather" #Provided URL of the server

  #Defining query parameters
  parameters = {
      "q": city,
      "appid":api_key,
      "units":"metric"
  }

  try:
    response = requests.get(url, params=parameters)
    return response.json()

  except requests.exceptions.HTTPError as http_err: #Captures HTTP error
    print(f"HTTP error: {http_err}")
  except requests.exceptions.RequestException as req_err: #Captures network error
    print(f"Network error: {req_err}")
  except Exception as e:  #Captures any error
    print(f"Unexpected error: {e}")
  
  return {}  # return empty dict in case of error

def analyze_weather(weather_data: dict): #Here the analyze_weather function is defined 
  """Analyzes weather data and returns a temperature summary with alerts."""
  if not weather_data or 'main' not in weather_data:
    return "No valid weather data to analyze."

  try:  #Extracts temperature, wind speed, and humidity. Uses .get() with defaults to avoid KeyErrors.
    print(weather_data) #Checkpoint
    temp = weather_data.get('main', {}).get('temp', 0)
    wind_speed = weather_data.get('wind', {}).get('speed', 0)
    humidity = weather_data['main'].get('humidity', 0)

  # Temperature Category
    if temp <= 10:
      summary = "Cold (≤10°C)"
    elif 11 <= temp <= 24:
      summary = "Mild (11–24°C)"
    else:
      summary = "Hot (≥25°C)"

  # Warnings
    warnings = []
    if wind_speed > 10:
      warnings.append("High wind alert!")
    if humidity > 80:
      warnings.append("Humid conditions!")

    return summary + (" | " + " ".join(warnings))

  except KeyError as e:
    return f"Missing data key: {e}"
  except Exception as e:
    return f"Error analyzing weather data: {e}"

def log_weather(city: str, filename: str):  #Logging the weather report
  """Fetches weather for a city and appends relevant data to a CSV file."""
  api_key = input("Enter your OpenWeatherMap API key: ").strip()
  weather = fetch_weather(city, api_key)

  if not weather or 'main' not in weather:
    print("No valid weather data to log.")
    return

  try:
    # Extract relevant data
    temp = weather['main'].get('temp', '')
    humidity = weather['main'].get('humidity', '')
    wind_speed = weather.get('wind', {}).get('speed', '')
    weather_desc = weather.get('weather', [{}])[0].get('description', '')

    # Prepare row
    row = [city, temp, humidity, wind_speed, weather_desc]

    # Write to CSV (append mode)
    file_exists = os.path.exists(filename)
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
      writer = csv.writer(file)
      if not file_exists or os.stat(filename).st_size == 0: #If the file does not exist automatically creates the file. If the file is empty begins writing the file with column heads
        writer.writerow(['City', 'Temperature (°C)', 'Humidity (%)', 'Wind Speed (m/s)', 'Weather Description'])
        writer.writerow(row)

      print(f"Weather for '{city}' logged to {filename}.")

  except Exception as e:
    print(f"Error writing to file: {e}")

#Main Program
if __name__ == "__main__":
  city = input("Enter city name: ")
  api_key = input("Enter your OpenWeatherMap API key: ")

  weather = fetch_weather(city, api_key)
  report = analyze_weather(weather)

  print("\nWeather Report:")
  print(report)

  log_weather(city,f"{city}_weather.csv")
