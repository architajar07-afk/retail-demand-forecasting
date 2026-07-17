# Calendar Data Integration

## Objective

The transformed sales dataset was integrated with the calendar dataset to enrich sales records with actual calendar information.

## Merge Process

The merge operation was performed using the common day identifier (`d`).

Additional attributes added:

- date
- weekday
- month
- year

## Result

Each sales record now contains both transactional information and calendar attributes.

This enables:

- Time-series forecasting
- Weekend analysis
- Monthly analysis
- Holiday analysis
- Seasonal trend analysis

## Business Value

Joining sales data with calendar information improves analytical capability and prepares the dataset for cloud data warehousing, SQL analysis, and forecasting.

## Next Steps

The enriched dataset will be loaded into BigQuery where SQL transformations and feature engineering will be performed.