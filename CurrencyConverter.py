import requests

class CurrencyConverter:
    def __init__(self):
        self.API_URL = "https://theforexapi.com/api/latest"
        self.api_key = "your_api_key"

    def convert(self, from_currency, to_currency, amount):
        params = {"base": from_currency, "symbols": to_currency, "rtype": "fpy", "apikey": self.api_key}
        response = requests.get(self.API_URL, params=params, verify=False)
        data = response.json()

        if "rates" in data:
            exchange_rate = data["rates"][to_currency]
            converted_amount = exchange_rate * amount
            return round(converted_amount, 2)
        else:
            raise ValueError("Could not retrieve exchange rate")

converter = CurrencyConverter()
amount = float(input("Enter amount to convert: "))
from_currency = input("Enter from currency: ").upper()
to_currency = input("Enter to currency: ").upper()

converted_amount = converter.convert(from_currency, to_currency, amount)
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
