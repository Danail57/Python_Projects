import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

class WeatherApp:
    def __init__(self):
        self.country = None
        self.city = None
        self.forecast = None

    def menu_forecast(self):
        while True:
            print("\nWelcome to Weather Application")
            print("Menu:\n1. Select country\n2. Select city\n3. Show Forecast\n4. Exit")
            try:
                command = int(input("Enter a number from 1 to 4: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if command == 1:
                self.select_country()
            elif command == 2:
                self.select_city()
            elif command == 3:
                self.show_forecast()
            elif command == 4:
                print("Exiting...")
                break
            else:
                print("Invalid command. Try again.")

    def select_country(self):
        try:
            with open("countries.txt", "r") as f:
                countries = [line.strip() for line in f]
        except FileNotFoundError:
            print("countries.txt not found!")
            return

        print("Available countries:", countries)
        choice = input("Enter a country: ")
        if choice in countries:
            self.country = choice
        else:
            print("No country selected or invalid country.")

    def select_city(self):
        if not self.country:
            print("You must select a country first.")
            return

        try:
            with open("towns.txt", "r") as f:
                towns = [line.strip() for line in f if self.country in line]
        except FileNotFoundError:
            print("towns.txt not found!")
            return

        print("Available cities:", towns)
        choice = input("Enter a city: ")
        if choice in towns:
            self.city = choice
        else:
            print("No city selected or invalid city.")

    def show_forecast(self):
        if not self.country or not self.city:
            print("You must select a country and a city first.")
            return

        params = {
            "q": f"{self.city},{self.country}",
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            weather_desc = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            print(f"Weather in {self.city}, {self.country}:")
            print(f"Temperature: {temp}°C")
            print(f"Description: {weather_desc}")
            print(f"Humidity: {humidity}%")
        else:
            print("Could not fetch weather data. Check city/country or API key.")

app = WeatherApp()
app.menu_forecast()
