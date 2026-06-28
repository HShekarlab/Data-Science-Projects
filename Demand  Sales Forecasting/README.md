# Rossmann Store Sales Forecasting

## Project Overview

This project develops an end-to-end retail sales forecasting pipeline using the Rossmann Store Sales dataset.

The objective is to predict future daily sales for Rossmann stores by leveraging historical sales patterns, promotional activities, competition information, and calendar-based features.

The project covers the complete machine learning workflow, including data cleaning, exploratory data analysis (EDA), feature engineering, model development, model evaluation, and submission file generation.

---

## Business Problem

Accurate sales forecasting is critical for retail operations.

Reliable forecasts help businesses optimize:

* Inventory management
* Workforce planning
* Promotional campaigns
* Supply chain operations
* Revenue forecasting

The goal is to estimate future sales for each store-day combination while minimizing forecasting error.

---

## Dataset

The project uses the Rossmann Store Sales dataset.

### Files

* `train.csv` – Historical sales data
* `test.csv` – Future periods requiring prediction
* `store.csv` – Store metadata
* `sample_submission.csv` – Competition submission format

### Main Features

| Feature             | Description                    |
| ------------------- | ------------------------------ |
| Store               | Store identifier               |
| Date                | Observation date               |
| Sales               | Daily sales (target variable)  |
| Customers           | Number of customers            |
| Promo               | Promotion indicator            |
| StateHoliday        | State holiday information      |
| SchoolHoliday       | School holiday indicator       |
| CompetitionDistance | Distance to nearest competitor |
| StoreType           | Store category                 |
| Assortment          | Product assortment level       |

---

## Project Workflow

### 1. Data Cleaning

* Loaded datasets using Polars
* Handled missing values
* Corrected data types
* Validated feature consistency

### 2. Exploratory Data Analysis (EDA)

Explored:

* Sales distribution
* Open vs closed store behavior
* Promotional effects
* Seasonal trends
* Store-level differences
* Competition impact

### 3. Feature Engineering

Created several forecasting features:

#### Date Features

* Year
* Month
* Weekday
* DayOfYear
* WeekOfYear

#### Cyclical Features

* Month_sin
* Month_cos
* Weekday_sin
* Weekday_cos

#### Competition Features

* HasCompetition
* CompetitionAgeMonths

#### Promotion Features

* Promo2AgeMonths

#### Historical Demand Features

* lag_1
* lag_7
* lag_30
* rolling_mean_7

---

## Model Development

### Baseline Model

LightGBM Regressor

### Hyperparameter Tuning

Experimented with:

* learning_rate
* num_leaves
* max_depth
* subsample
* colsample_bytree

Model selection was based on forecasting performance and RMSPE.

---

## Evaluation Metrics

The following metrics were used:

* RMSE (Root Mean Squared Error)
* MAE (Mean Absolute Error)
* RMSPE (Root Mean Squared Percentage Error)

RMSPE was selected as the primary metric because it is the official evaluation metric of the Rossmann competition.

---

## Results

### Baseline Model

| Metric |  Score |
| ------ | -----: |
| RMSE   | 723.25 |
| MAE    | 483.99 |
| RMSPE  | 0.1188 |

### Tuned Model

| Metric |  Score |
| ------ | -----: |
| RMSE   | 722.56 |
| MAE    | 503.72 |
| RMSPE  | 0.1214 |

The baseline model achieved superior RMSPE performance and was selected as the final forecasting model.

---

## Feature Importance

The most influential features included:

* DayOfYear
* lag_7
* rolling_mean_7
* lag_1
* DayOfWeek
* CompetitionDistance
* Promo

Results indicate that historical demand patterns were the strongest predictors of future sales.

---

## Key Findings

* Historical sales signals significantly improve forecasting accuracy.
* Promotional campaigns strongly influence sales volume.
* Competition-related variables contribute meaningful predictive power.
* Feature engineering had a larger impact than hyperparameter tuning.
* RMSPE provides a more realistic evaluation framework for retail forecasting.

---

## Technologies Used

* Python
* Polars
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* LightGBM

---

## Future Improvements

Potential future enhancements include:

* Time-series cross-validation
* Optuna-based hyperparameter optimization
* Ensemble models
* Advanced lag feature generation for inference
* Store-specific forecasting models

---

## Conclusion

This project demonstrates a complete machine learning workflow for retail demand forecasting.

The final solution successfully combines business understanding, feature engineering, model interpretation, and predictive modeling to generate accurate store-level sales forecasts.
