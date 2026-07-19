# BigQuery Setup

## Completed
- Created Google Cloud project.
- Created BigQuery dataset: retail_forecasting.
- Successfully imported calendar.csv into BigQuery.

## Observation
The remaining datasets (sell_prices.csv and sales_train_evaluation.csv) exceed the 100 MB local upload limit in BigQuery Sandbox.

Cloud Storage upload requires billing, so the project will continue using local processing with Pandas while retaining the BigQuery setup for demonstration purposes.

## Next Steps
- Continue feature engineering using Pandas.
- Build forecasting dataset.
- Train forecasting model.