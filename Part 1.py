'''breakdown for exchange calculator:

*before coding, import the CSV into python (here) to give python a reference point*

    1. user wants to know how much a specific dollar amount (either CAD or USD) is worth in the opposite currency
        a) i.e., FROM $80 CAD TO USD
		b) *user can input a number with a comma (i.e., 1,000) and python will still read it as a number (1000)*
    2. python opens the CSV file
    3. python finds the row and column for the most recent exchange rate (2025)
    4. print the exact DOLLAR amount in their desired currency
	5. print the exact RATE of exchange
'''

import csv

class ExchangeRates:
	def __init__(self):
		self.filename = "BankOfCanadaExchangeRate.2026.csv"
		self.exchangeNumber = None # These two variables below are set to None (placeholder for now) so that they can be defined later when Python actually reads the CSV file
		self.year = None
		self.read_rate() # The read_rate() function is used to read the exchange rate from the CSV file and set the exchangeNumber and year variables
		
	def read_rate(self):
		with open(self.filename, "r") as f: 
			lines = csv.reader(f) # Reads the CSV file and separates its contents into rows and columns
			data = list(lines) # Converts the CSV contents into a list so specific values can be accessed
			self.exchangeNumber = float(data[-1][26])
			self.year = int(data[-1][0][:4]) # This prompts the code to search for the value in this specific row/column
			# (the exchange rate for 2025, which is the most recent year in the CSV file = 1.3978)
			
	def convert(self):
			moneyAmt = float(input("How much money?: $").replace(",", "")) # .replace(",","") lets the user input a number with a comma (i.e., 1,000) and Python will still read it as a number (1000)
			moneyFrom = (input("What currency are you exchanging from (USD or CAD): ").upper()) # .upper() lets Python read the user's input as either USD or CAD, regardless of whether they type it in lowercase or uppercase
			moneyTo = (input("What currency are you exchanging to (USD or CAD): ").upper())

			if (moneyFrom == "USD"):
				moneyFinal =  moneyAmt * self.exchangeNumber # Formula for USD to CAD conversion
				print(f"Your final money is: CAD  ${moneyFinal:,.2f} | "
				      f"The exchange rate used ({self.year}): {self.exchangeNumber}")
			else:
				moneyFinal = moneyAmt / self.exchangeNumber # Formula for CAD to USD conversion
				print(f"Your final money is: USD  ${moneyFinal:,.2f} | "
				      f"The exchange rate used ({self.year}): {self.exchangeNumber}")

calculator = ExchangeRates() # Creates an object called calculator using the ExchangeRates class
calculator.convert() # Calls the convert() method to ask for user inputs and perform the currency conversion
