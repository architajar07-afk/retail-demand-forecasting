import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# -----------------------------
# Project Paths
# -----------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DATA = PROJECT_ROOT / "data" / "raw"

FIGURES = PROJECT_ROOT / "reports" / "figures"

FIGURES.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Load datasets
# -----------------------------

sales = pd.read_csv(RAW_DATA / "sales_train_evaluation.csv")
calendar = pd.read_csv(RAW_DATA / "calendar.csv")

print("Datasets loaded successfully.")

# -----------------------------
# Daily Sales
# -----------------------------

daily_sales = sales.iloc[:, 6:].sum()

sales_trend = pd.DataFrame({
    "d": daily_sales.index,
    "sales": daily_sales.values
})

sales_trend = sales_trend.merge(
    calendar[["d", "date"]],
    on="d"
)

sales_trend["date"] = pd.to_datetime(
    sales_trend["date"]
)

# -----------------------------
# Plot
# -----------------------------

plt.figure(figsize=(14,6))

plt.plot(
    sales_trend["date"],
    sales_trend["sales"],
    linewidth=1
)

plt.title("Total Daily Sales Trend")

plt.xlabel("Date")

plt.ylabel("Units Sold")

plt.tight_layout()

plt.savefig(
    FIGURES / "daily_sales_trend.png"
)

plt.close()

print("Created: daily_sales_trend.png")

# -----------------------------
# Statistics
# -----------------------------

print("\nSales Statistics")

print(sales_trend["sales"].describe())