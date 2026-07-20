import pandas as pd

calendar = pd.read_csv("data/raw/calendar.csv")
sales = pd.read_csv("data/raw/sales_train_evaluation.csv")
prices = pd.read_csv("data/raw/sell_prices.csv")

print("Calendar:", calendar.shape)
print("Sales:", sales.shape)
print("Prices:", prices.shape)

print(calendar.head())

print(sales.head())

print(prices.head())

print(calendar.isnull().sum())

print(prices.isnull().sum())

print(sales.isnull().sum())