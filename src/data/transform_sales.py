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
# Load Dataset
# -----------------------------

sales = pd.read_csv(
    RAW_DATA / "sales_train_evaluation.csv"
)

print("Dataset loaded.")

# -----------------------------
# Sample Dataset
# -----------------------------

sales_sample = sales.head(1000)

print(f"Sample size: {sales_sample.shape}")

# -----------------------------
# Wide → Long Transformation
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

print("\nTransformation Complete")

print(sales_long.head())

print("\nShape")

print(sales_long.shape)

# -----------------------------
# Save
# -----------------------------

output_file = PROCESSED_DATA / "sales_long_sample.csv"

sales_long.to_csv(
    output_file,
    index=False
)

print("\nSaved to:")

print(output_file)

