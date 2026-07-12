import pandas as pd
from pathlib import Path

# Define project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

# Dataset file paths
calendar_path = RAW_DATA_DIR / "calendar.csv"
sales_path = RAW_DATA_DIR / "sales_train_evaluation.csv"
prices_path = RAW_DATA_DIR / "sell_prices.csv"

# Load datasets
calendar = pd.read_csv(calendar_path)
sales = pd.read_csv(sales_path)
prices = pd.read_csv(prices_path)

print("\n=== CALENDAR DATASET ===")
print("Shape:", calendar.shape)
print("\nColumns:")
print(calendar.columns.tolist())
print("\nFirst 5 rows:")
print(calendar.head())
print("\nMissing values:")
print(calendar.isnull().sum())

print("\n=== SALES DATASET ===")
print("Shape:", sales.shape)
print("\nFirst 10 columns:")
print(sales.columns[:10].tolist())
print("\nFirst 5 rows:")
print(sales.head())

print("\n=== SELL PRICES DATASET ===")
print("Shape:", prices.shape)
print("\nColumns:")
print(prices.columns.tolist())
print("\nFirst 5 rows:")
print(prices.head())
print("\nMissing values:")
print(prices.isnull().sum())