import requests

API_KEY = "a1b2c3d4e5f67890abcdef1234567890"

from_currency = input("From Currency (e.g. USD): ").upper()
to_currency = input("To Currency (e.g. INR): ").upper()
amount = float(input("Enter Amount: "))

url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    if data["result"] == "success":

        exchange_rate = data["conversion_rates"][to_currency]

        converted_amount = amount * exchange_rate

        print("\n====== Currency Converter ======")
        print("From Currency :", from_currency)
        print("To Currency   :", to_currency)
        print("Amount        :", amount)
        print("Exchange Rate :", exchange_rate)
        print("Converted     :", round(converted_amount, 2))

    else:
        print("Invalid Currency Code")

else:
    print("Something Went Wrong")