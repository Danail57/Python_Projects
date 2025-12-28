# Work in progress
class WeatherApp:
    def __init__(self):
        self.forecast = None
        self.country = None
        self.city = None

    def menu_forecast(self):
        print("Welcome to Weather Application")
        print("Menu:\n1. Select country\n2. Select city\n3. Show Forecast\n4. Exit")

        permissioned_commands = [1, 2, 3, 4]

        command = int(input("Enter a number from 1 to 4:"))

        if command not in permissioned_commands:
            raise ValueError("Invalid input. Please enter a number from the given list.")

        if command == 1:
            with open("countries.txt", "r") as f:
                countries = [line.strip() for line in f]
            print("Available countries:", countries)

            choice = input("Enter a country: ")
            if choice in countries:
                self.country = choice
            else:
                raise ValueError("No country selected.")


        elif command == 2:
            if not self.country:
                print("You must select a country first.")
                return
            with open("towns.txt", "r") as f:
                towns = [line.strip() for line in f if self.country in line]
            print("Available cities:", towns)

            choice = input("Enter a city: ")
            if choice in towns:
                self.city = choice
            else:
                raise ValueError("No town selected.")

        elif command == 3:
            if not self.country or not self.city:
                print("You must select a country and a city first.")
            else:
                print("Available cities:", self.country, self.city)

app = WeatherApp()
app.menu_forecast()


class API:
    info_data = {
        "Bulgaria": "Sofia",
        "USA": "Washington D.C.",
        "Canada": "Ottawa",
        "UK": "London"
    }

    def __init__(self, city: str, country: str):
        self.city = city
        self.country = country

    def show_info(self):
        if self.city not in self.info_data:
            print("No data found for this city.")
        else:
            print(f"City for {self.city}: {self.info_data[self.city]}")


    if not info_data:

        print("No data found.")
