# 💰 Medical Insurance Cost Prediction

Machine Learning project for predicting individual medical insurance costs using demographic, lifestyle, and health-related factors.

---

## 📖 Overview

Healthcare expenses vary significantly between individuals due to factors such as age, BMI, smoking habits, family size, and geographic location.

This project applies machine learning techniques to estimate medical insurance charges based on patient characteristics and identify the factors that contribute most to healthcare costs.

The project demonstrates a complete regression workflow from exploratory analysis to predictive modeling.

---

## 🎯 Business Problem

Accurately estimating medical costs is important for:

🏥 Insurance Providers

📊 Risk Assessment Teams

💰 Pricing Analysts

📈 Healthcare Policy Planning

The objective is to build a regression model capable of predicting future medical insurance charges based on customer information.

---

## 📊 Dataset Features

| Feature | Description |
|----------|------------|
| Age | Age of the insured individual |
| Sex | Gender |
| BMI | Body Mass Index |
| Children | Number of dependents |
| Smoker | Smoking status |
| Region | Residential region |
| Charges | Medical insurance cost (Target) |

---

## 🔍 Exploratory Data Analysis

A comprehensive analysis was performed to understand the relationships between features and insurance charges.

### 📈 Distribution Analysis

- Age Distribution
- BMI Distribution
- Insurance Charges Distribution

### 📊 Feature Relationships

- Charges vs Age
- Charges vs BMI
- Charges vs Smoking Status
- Charges vs Number of Children

### 🔥 Correlation Analysis

- Feature Correlations
- Cost Drivers Identification

---

## 🧹 Data Preprocessing

### Data Cleaning

- Missing Value Inspection
- Data Validation

### Feature Encoding

Categorical features such as:

```text
Sex
Smoker
Region
```

were converted into machine-readable numerical representations.

### Feature Scaling

Numerical variables were standardized to improve model performance.

---

## 🤖 Machine Learning Pipeline

The project follows a supervised learning regression approach.

### Training Workflow

```text
Data Collection
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
Train/Test Split
      ↓
Model Training
      ↓
Performance Evaluation
```

---

## 📏 Evaluation Metrics

Model performance was assessed using:

### MAE

```text
Mean Absolute Error
```

### MSE

```text
Mean Squared Error
```

### RMSE

```text
Root Mean Squared Error
```

### R² Score

```text
Coefficient of Determination
```

These metrics provide insight into prediction accuracy and model reliability.

---

## 💡 Key Insights

The analysis highlights several important observations:

✅ Smoking status has a major impact on medical expenses.

✅ Higher BMI is often associated with increased healthcare costs.

✅ Age is a strong predictor of insurance charges.

✅ Family size can influence total healthcare expenditure.

---

## 🛠 Tech Stack

### Data Analysis

📊 Pandas

🔢 NumPy

📉 Matplotlib

🎨 Seaborn

### Machine Learning

🤖 Scikit-Learn

### Development Environment

🐍 Python

📓 Jupyter Notebook

---

## 📂 Project Structure

```text
├── Medical Cost Prediction.ipynb
├── insurance.csv
├── README.md
```

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/your-username/medical-cost-prediction.git
```

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Run Notebook

```bash
jupyter notebook
```

Open:

```text
Medical Cost Prediction.ipynb
```

and execute all notebook cells.

---

## 📚 Skills Demonstrated

✅ Exploratory Data Analysis (EDA)

✅ Feature Engineering

✅ Regression Modeling

✅ Healthcare Analytics

✅ Data Visualization

✅ Model Evaluation

✅ Predictive Analytics

---

## 🔮 Future Improvements

Potential extensions include:

- Random Forest Regressor
- XGBoost Regressor
- LightGBM
- Hyperparameter Optimization
- Feature Importance Analysis
- SHAP Explainability
- Web Deployment with FastAPI

---

## 🌟 Learning Journey

This repository represents one of my early machine learning projects focused on healthcare analytics and regression modeling.

The project helped strengthen my understanding of predictive modeling, feature analysis, and real-world business applications of machine learning.

---

### ⭐ If you find this project useful, feel free to star the repository.
