## FINE3300-2026-A1-Shiva-Moslemin-Asl

## Project Overview

This project is a USD/CAD currency exchange calculator. The program reads annual exchange rate data from the provided `BankOfCanadaExchangeRate.2026.csv` file and uses the most recent available USD/CAD exchange rate to convert amounts between United States dollars and Canadian dollars.

The assignment is divided into two parts. Part 1 contains the version of the calculator that I created myself, while Part 2 contains a separate version generated using an AI model that I compare my work to.

## Part 1: Shiva's Currency Exchange Calculator

For Part 1, I created a Python program (found in the `Part 1.py` folder) that allows the user to:

- Enter any amount of money to convert (with or without commas, however many decimal points)
- Convert USD to CAD or vice versa
- Enter currency codes using uppercase or lowercase letters (Python will recognize both)
- Print the converted amount with dollar signs, commas, and two decimal places for the user
- Print the exchange rate and year used in the calculation

## Part 2: AI-Generated Currency Exchange Calculator + Comparison with Shiva's Code

For Part 2, I use ChatGPT-5.6 Sol to generate a separate version of the currency exchange calculator from scratch. The AI is provided with the assignment requirements (summarized in my own words) and the same `BankOfCanadaExchangeRate.2026.csv` dataset.

The AI-generated version is saved as a separate folder titled `ExchangeRatesAI.py` and tested here in Visual Studio Code.