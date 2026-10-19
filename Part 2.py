# ExchangeRatesAI.py
# Comparison of Shiva's code vs. ChatGPT's code:
'''
I provided the model with the CSV file, "BankOfCanadaExchangeRate.2026.csv", so it could determine the structure of the dataset and
identify the appropriate USD/CAD exchange rate. After testing the initial code, I found that it had trouble correctly reading the
"Date" column from the CSV file, which caused a 'KeyError' when the program tried to retrieve the year. The model would also try to import
additional modules like 'pathlib' (from pathlib import Path), which I did not want to use because I was not familiar with them. After fixing
that error, the code below is the final output that ChatGPT generated for me.

In terms of comparison, the AI code is longer and uses some syntax that I did not learn and would not have thought to use on my own. For example,
it uses 'csv.DictReader' to read the CSV file as a dictionary, which means the code can refer to a column by its name, such as "FXAUSDCAD",
instead of having to remember which column number it is in. 

Additionally, the AI version passes 'source_currency' and 'target_currency' directly into the conversion method, so they are only used when a
conversion is being made from user input. In my version, I ask for 'moneyFrom' and 'moneyTo' inside the convert() method and then use
'moneyFrom' to determine whether the exchange rate should be multiplied or divided. 

Overall, The AI version separates more steps and uses more variables and methods, which makes it more structured, but also a little more complex
than the Python concepts I learned and used in my own version.
'''

import csv


class ExchangeRatesAI:

    def __init__(self):
        self.filename = "BankOfCanadaExchangeRate.2026.csv"
        self.rate = None
        self.year = None
        self.load_exchange_rate()

    def load_exchange_rate(self):
        with open(self.filename, "r", encoding="utf-8-sig") as file: # What is "utf-8-sig"???
            reader = csv.DictReader(file)
            rows = list(reader)

            latest = rows[-1]

            self.rate = float(latest["FXAUSDCAD"])
            self.year = latest["Date"][:4]

    def convert_currency(self, amount, source_currency, target_currency):

        if source_currency == "USD" and target_currency == "CAD":
            return amount * self.rate

        if source_currency == "CAD" and target_currency == "USD":
            return amount / self.rate

        return None


exchange = ExchangeRatesAI()

amount = float(input("Amount: ").replace(",", ""))

source = input("Source currency (USD/CAD): ").upper()
target = input("Target currency (USD/CAD): ").upper()

converted = exchange.convert_currency(amount, source, target)

if converted is not None:
    print()
    print("Conversion Result")
    print("-----------------")
    print(f"Input: {source} {amount:,.2f}")
    print(f"Output: {target} {converted:,.2f}")
    print(f"Rate: {exchange.rate}")
    print(f"Rate Year: {exchange.year}")

else:
    print("Invalid currency pair.")