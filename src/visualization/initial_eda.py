import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Define project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"

# Ensure figures directory exists
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# Load datasets
sales = pd.read_csv(
    RAW_DATA_DIR / "sales_train_evaluation.csv"
)

prices = pd.read_csv(
    RAW_DATA_DIR / "sell_prices.csv"
)

print("Datasets loaded successfully.")

# --------------------------------------------------
# 1. Products by Category
# --------------------------------------------------

category_counts = (
    sales.groupby("cat_id")["item_id"]
    .nunique()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
category_counts.plot(kind="bar")

plt.title("Number of Products by Category")
plt.xlabel("Category")
plt.ylabel("Number of Unique Products")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "products_by_category.png"
)

plt.close()

print("Created: products_by_category.png")


# --------------------------------------------------
# 2. Products by Department
# --------------------------------------------------

department_counts = (
    sales.groupby("dept_id")["item_id"]
    .nunique()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 5))
department_counts.plot(kind="bar")

plt.title("Number of Products by Department")
plt.xlabel("Department")
plt.ylabel("Number of Unique Products")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "products_by_department.png"
)

plt.close()

print("Created: products_by_department.png")


# --------------------------------------------------
# 3. Product Records by Store
# --------------------------------------------------

store_counts = (
    sales["store_id"]
    .value_counts()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 5))
store_counts.plot(kind="bar")

plt.title("Product Records by Store")
plt.xlabel("Store")
plt.ylabel("Number of Product Records")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "products_by_store.png"
)

plt.close()

print("Created: products_by_store.png")


# --------------------------------------------------
# 4. Sell Price Distribution
# --------------------------------------------------

plt.figure(figsize=(10, 5))

plt.hist(
    prices["sell_price"],
    bins=50
)

plt.title("Distribution of Product Sell Prices")
plt.xlabel("Sell Price")
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "sell_price_distribution.png"
)

plt.close()

print("Created: sell_price_distribution.png")


print("\nInitial EDA visualizations completed successfully.")