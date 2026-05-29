# 📊 Customer Churn Prediction

This project focuses on predicting customer churn using supervised machine learning techniques.  
The goal is to identify customers who are likely to discontinue the service, enabling proactive and data-driven retention strategies.

The project is implemented as an end-to-end machine learning workflow, from exploratory data analysis to model interpretation.

---

## 🧠 Problem Overview

Customer churn prediction is a binary classification problem where the objective is to correctly identify customers who are at risk of leaving the service.

- **Target variable:** `Churn` (Yes / No)
- **Type of problem:** Binary classification
- **Business focus:** Minimizing missed churn cases (false negatives)

---

## 📁 Dataset

The dataset contains customer-level information related to:
- Demographics
- Subscribed services
- Contract and payment details
- Account-level usage information

The target variable indicates whether a customer has churned.

---

## 🔍 Exploratory Data Analysis (EDA)

Exploratory data analysis was conducted to:
- Examine the distribution of the target variable
- Analyze numerical features such as tenure and charges
- Explore relationships between categorical features and churn behavior

Key insights from EDA informed preprocessing and modeling decisions.

---

## 🛠️ Data Preprocessing

The following preprocessing steps were applied:

- Train-test split to ensure unbiased evaluation
- Encoding of categorical variables
- Feature scaling for numerical variables
- Handling class imbalance to improve churn detection

All preprocessing steps were integrated into a unified pipeline to prevent data leakage.

---

## 🤖 Modeling Approach

### Baseline Model
A logistic regression model was used as the baseline due to:
- Its simplicity
- Interpretability
- Suitability for binary classification problems

### Threshold Optimization
Decision threshold tuning was performed to improve recall for the churn class, aligning model predictions with business priorities.

---

## 📊 Model Comparison

Multiple models were evaluated using consistent preprocessing and the same test set:

- Logistic Regression (class-weighted)
- Random Forest
- Gradient Boosting

### Evaluation Metrics
Models were compared using:
- **Recall (Churn class)** — primary metric
- **ROC AUC** — overall discrimination ability
- **Accuracy** — secondary reference metric

The comparison results motivated the selection of the final model.

---

## ✅ Final Model Selection

A **class-weighted logistic regression** model was selected as the final model due to:

- Strong recall performance on the churn class
- Competitive ROC AUC
- High interpretability compared to more complex models

This balance makes the model suitable for real-world business applications.

---

## 🔎 Feature Importance & Interpretation

Feature importance analysis was conducted on the final model to understand key drivers of churn.

The analysis highlighted several influential factors, such as:
- Contract type
- Customer tenure
- Monthly charges
- Availability of support-related services

These insights enable translation of model results into actionable business understanding.

---

## 🎨 Visualization Design

A consistent color palette inspired by CRM systems was used across all visualizations to:
- Clearly distinguish churn vs. non-churn customers
- Maintain visual consistency throughout the notebook
- Enhance interpretability of comparative plots

---

## 🧾 Project Structure

- `Customer Churn Prediction.ipynb` — main notebook containing the full analysis
- `README.md` — project overview and documentation

---

## 🔮 Future Improvements

Potential future enhancements include:
- Additional feature engineering
- Hyperparameter tuning
- Cross-validation for robustness assessment
- Testing alternative imbalance-handling strategies

---

## 📌 Conclusion

This project demonstrates a complete and structured approach to customer churn prediction, combining sound data analysis, thoughtful model evaluation, and interpretability.  
The final model provides a practical balance between performance and transparency, making it suitable for deployment-oriented scenarios.
