import pandas as pd

calendar = pd.read_csv("data/raw/calendar.csv")
sales = pd.read_csv("data/raw/sales_train_evaluation.csv")
prices = pd.read_csv("data/raw/sell_prices.csv")

sales_long = sales.melt(
    id_vars=[
        "id",
        "item_id",
        "dept_id",
        "cat_id",
        "store_id",
        "state_id",
    ],
    var_name="d",
    value_name="sales"
)

merged = sales_long.merge(calendar, on="d", how="left")

merged["date"] = pd.to_datetime(merged["date"])

merged["year"] = merged["date"].dt.year
merged["month"] = merged["date"].dt.month
merged["day"] = merged["date"].dt.day
merged["day_of_week"] = merged["date"].dt.dayofweek
merged["week"] = merged["date"].dt.isocalendar().week.astype(int)

merged = merged.merge(
    prices,
    on=["store_id", "item_id", "wm_yr_wk"],
    how="left"
)

merged["sell_price"] = merged["sell_price"].fillna(0)

print(merged[
    [
        "date",
        "year",
        "month",
        "day",
        "day_of_week",
        "week",
        "sell_price"
    ]
].head())

import os

os.makedirs("data/processed", exist_ok=True)

merged.head(1000).to_csv(
    "data/processed/feature_engineered_sample.csv",
    index=False
)
