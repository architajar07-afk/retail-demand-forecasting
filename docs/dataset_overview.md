# M5 Forecasting Dataset Overview

## Dataset Source

The M5 Forecasting dataset contains historical retail sales data used for demand forecasting and inventory analysis.
Three primary dataset files were selected for the project:

1. calendar.csv
2. sales_train_evaluation.csv
3. sell_prices.csv

## Calendar Dataset

Shape: 1,969 rows and 14 columns

The calendar dataset contains date-related information used to analyze sales patterns over time.

Important attributes include:

- date
- weekday
- month
- year
- event names
- event types
- SNAP indicators

Missing values were observed in the event-related columns. These values are expected because events do not occur on every calendar date.

## Sales Dataset

Shape: 30,490 rows and 1,947 columns

The sales dataset contains historical daily sales information for products across different stores.

Important identifiers include:

- item_id
- dept_id
- cat_id
- store_id
- state_id

Daily sales are stored in columns such as d_1, d_2, d_3, and subsequent day columns.

The dataset is currently stored in wide format. It will later be transformed into a long-format structure suitable for time-series analysis and forecasting.

## Sell Prices Dataset

Shape: 6,841,121 rows and 4 columns
The sell prices dataset contains weekly product pricing information.
Columns include:

- store_id
- item_id
- wm_yr_wk
- sell_price

This dataset will help analyze the relationship between product prices and customer demand.

## Initial Observations

- The dataset contains hierarchical retail sales data.
- Sales are available at item, department, category, store, and state levels.
- Calendar information can be used to analyze seasonality and event effects.
- Product pricing information can be used as a forecasting feature.
- The sales dataset requires transformation from wide format to long format before detailed time-series analysis.

## Next Steps

- Perform initial data quality checks.
- Analyze missing values and data types.
- Transform the sales dataset into a forecasting-friendly structure.
- Prepare the datasets for loading into the cloud data warehouse.

