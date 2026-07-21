import pandas as pd

calendar = pd.read_csv("data/raw/calendar.csv")
sales = pd.read_csv("data/raw/sales_train_evaluation.csv")

print("Calendar Shape:", calendar.shape)
print("Sales Shape:", sales.shape)

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

print(sales_long.head())
print(sales_long.shape)

merged = sales_long.merge(
    calendar,
    on="d",
    how="left"
)

print(merged.head())
print(merged.shape)

merged.head(1000).to_csv(
    "data/processed/forecasting_sample.csv",
    index=False
)