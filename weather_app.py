import requests

# OpenWeatherMap API Key (Replace with your actual API key)
API_KEY = "0a23d58d7153107cede530424a1edb58" 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetches weather data for a given city."""
    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}  # Get temperature in Celsius
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] != 200:
            print("Error:", data["message"])
            return

        # Extract relevant weather information
        city_name = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_condition = data["weather"][0]["description"]

        # Display weather details
        print(f"\n🌍 Weather in {city_name}:")
        print(f"🌡️ Temperature: {temperature}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"⛅ Condition: {weather_condition.capitalize()}")

    except requests.exceptions.RequestException as e:
        print("Network error. Please check your connection.")

# Main program loop
if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
