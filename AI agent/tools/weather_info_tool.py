import os
from utils.weather_info import WeatherForecastTool
from langchain.tools import tool
from typing import List
from dotenv import load_dotenv

class WeatherInfoTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
        self.weather_service = WeatherForecastTool(self.api_key)
        self.weather_tool_list = self._setup_tools()
    
    def _setup_tools(self) -> List:
        """Setup all tools for the weather forecast tool"""
        @tool
        def get_current_weather(city: str) -> str:
            """Get current weather for a city. Works with cities worldwide including India (e.g., 'Mumbai', 'Delhi', 'Mumbai,IN')"""
            weather_data = self.weather_service.get_current_weather(city)
            if weather_data and 'main' in weather_data:
                temp = weather_data.get('main', {}).get('temp', 'N/A')
                desc = weather_data.get('weather', [{}])[0].get('description', 'N/A')
                humidity = weather_data.get('main', {}).get('humidity', 'N/A')
                feels_like = weather_data.get('main', {}).get('feels_like', 'N/A')
                city_name = weather_data.get('name', city)
                country = weather_data.get('sys', {}).get('country', '')
                
                return f"Current weather in {city_name}, {country}: {temp}°C (feels like {feels_like}°C), {desc}, humidity: {humidity}%"
            elif weather_data and 'message' in weather_data:
                return f"Weather API Error for {city}: {weather_data['message']}. Try using format 'CityName,CountryCode' (e.g., 'Mumbai,IN')"
            return f"Could not fetch weather for {city}. Please check city name or try format 'CityName,CountryCode'"
        
        @tool
        def get_weather_forecast(city: str) -> str:
            """Get weather forecast for a city. Works with cities worldwide including India (e.g., 'Mumbai', 'Delhi', 'Mumbai,IN')"""
            forecast_data = self.weather_service.get_forecast_weather(city)
            if forecast_data and 'list' in forecast_data:
                city_name = forecast_data.get('city', {}).get('name', city)
                country = forecast_data.get('city', {}).get('country', '')
                
                forecast_summary = []
                for i in range(min(8, len(forecast_data['list']))):  # Limit to 8 entries
                    item = forecast_data['list'][i]
                    date_time = item['dt_txt']
                    date = date_time.split(' ')[0]
                    time = date_time.split(' ')[1]
                    temp = item['main']['temp']
                    desc = item['weather'][0]['description']
                    forecast_summary.append(f"{date} {time}: {temp}°C, {desc}")
                
                return f"Weather forecast for {city_name}, {country}:\n" + "\n".join(forecast_summary)
            elif forecast_data and 'message' in forecast_data:
                return f"Forecast API Error for {city}: {forecast_data['message']}. Try using format 'CityName,CountryCode' (e.g., 'Mumbai,IN')"
            return f"Could not fetch forecast for {city}. Please check city name or try format 'CityName,CountryCode'"
    
        return [get_current_weather, get_weather_forecast]