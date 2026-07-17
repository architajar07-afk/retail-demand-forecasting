import pandas as pd
from pathlib import Path

# -----------------------------
# Project Paths
# -----------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DATA = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed"

PROCESSED_DATA.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Load datasets
# -----------------------------

sales = pd.read_csv(
    RAW_DATA / "sales_train_evaluation.csv"
)

calendar = pd.read_csv(
    RAW_DATA / "calendar.csv"
)

print("Datasets loaded successfully.")

# -----------------------------
# Smaller sample
# -----------------------------

sales_sample = sales.head(100)

# -----------------------------
# Wide → Long
# -----------------------------

sales_long = pd.melt(
    sales_sample,
    id_vars=[
        "id",
        "item_id",
        "dept_id",
        "cat_id",
        "store_id",
        "state_id"
    ],
    var_name="d",
    value_name="sales"
)

# -----------------------------
# Merge with calendar
# -----------------------------

merged = sales_long.merge(
    calendar[["d", "date", "weekday", "month", "year"]],
    on="d",
    how="left"
)

print("\nMerged Dataset")

print(merged.head())

print("\nShape")

print(merged.shape)

# -----------------------------
# Save
# -----------------------------

output_file = PROCESSED_DATA / "sales_with_calendar_sample.csv"

merged.to_csv(
    output_file,
    index=False
)

print("\nSaved to:")

print(output_file)