from bs4 import BeautifulSoup
import requests

# List of cities to scrape weather data for
cities = ["New York", "London", "Paris", "Berlin"]

# Scrape weather data for each city
for city in cities:
  # Send an HTTP request to the weather website
  response = requests.get(f"https://www.weather.com/weather/today/{city}")

  # Parse the HTML response using BeautifulSoup
  soup = BeautifulSoup(response.text, "html.parser")

  # Extract the current temperature
  temperature = soup.find("span", {"class": "temperature-value"}).text

  # Print the city and temperature
  print(f"The temperature in {city} is {temperature}")
