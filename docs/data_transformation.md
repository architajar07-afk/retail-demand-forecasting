 # Wide-to-Long Data Transformation

## Objective

The original sales dataset stored daily sales across 1,941 separate columns.

While suitable for storage, this format is inefficient for analytics, SQL querying, and forecasting.

The objective of this transformation was to convert the dataset into a long-format structure.

---

## Transformation Method

The Pandas `melt()` function was used.

Identifier columns were retained:

- id
- item_id
- dept_id
- cat_id
- store_id
- state_id

Daily sales columns were transformed into:

- d
- sales

---

## Result

Original sample:

- Rows: 1,000
- Columns: 1,947

Transformed sample:

- Rows: 1,941,000
- Columns: 8

Each row now represents the sales of a single product on a single day.

---

## Benefits

The transformed dataset is better suited for:

- SQL analysis
- BigQuery
- Time-series forecasting
- Machine Learning
- Dashboard development

---

## Next Steps

The transformed data will later be merged with the calendar dataset to replace day identifiers (d_1, d_2, etc.) with actual calendar dates.

Additional feature engineering will then be performed before model development.