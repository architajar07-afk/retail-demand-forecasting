import pandas as pd
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA = PROJECT_ROOT / "data" / "raw"

# Load datasets
sales = pd.read_csv(RAW_DATA / "sales_train_evaluation.csv")
calendar = pd.read_csv(RAW_DATA / "calendar.csv")
prices = pd.read_csv(RAW_DATA / "sell_prices.csv")

print("=" * 60)
print("M5 DATASET SUMMARY")
print("=" * 60)

print("\nNumber of products:")
print(sales["item_id"].nunique())

print("\nNumber of departments:")
print(sales["dept_id"].nunique())

print("\nNumber of categories:")
print(sales["cat_id"].nunique())

print("\nNumber of stores:")
print(sales["store_id"].nunique())

print("\nNumber of states:")
print(sales["state_id"].nunique())

print("\nStore Names:")
print(sales["store_id"].unique())

print("\nState Names:")
print(sales["state_id"].unique())

print("\nCategories:")
print(sales["cat_id"].unique())

print("\nDepartments:")
print(sales["dept_id"].unique())

print("\nCalendar Date Range")
print(calendar["date"].min())
print(calendar["date"].max())

print("\nPrice Statistics")
print(prices["sell_price"].describe())