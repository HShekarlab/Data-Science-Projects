# 💳 Credit Card Fraud Detection using Machine Learning

> **An end-to-end Machine Learning project for detecting fraudulent credit card transactions, covering the complete ML lifecycle from exploratory data analysis to production-ready deployment using FastAPI.**

---

# 📖 Table of Contents

* Project Overview
* Problem Statement
* Objectives
* Dataset
* Project Workflow
* Exploratory Data Analysis
* Data Preprocessing
* Machine Learning Models
* Model Evaluation
* Hyperparameter Optimization
* Model Explainability (SHAP)
* Threshold Optimization
* Cost-sensitive Evaluation
* Production Pipeline
* FastAPI Deployment
* Project Structure
* Installation
* API Usage
* Technologies Used
* Future Improvements
* Author

---

# 📌 Project Overview

Credit card fraud detection is one of the most challenging problems in financial machine learning due to the extremely imbalanced nature of the data.

In real-world payment systems, fraudulent transactions represent only a tiny fraction of all operations. Consequently, traditional evaluation metrics such as Accuracy are often misleading, making Precision, Recall, ROC-AUC, and Precision-Recall analysis significantly more informative.

This project demonstrates a complete end-to-end Machine Learning workflow, including:

* Exploratory Data Analysis (EDA)
* Data Preprocessing
* Model Comparison
* Hyperparameter Optimization
* Model Explainability
* Threshold Optimization
* Cost-sensitive Evaluation
* Production Pipeline
* REST API Deployment

The final solution is packaged as a reusable Scikit-Learn Pipeline and deployed through FastAPI.

---

# 🎯 Problem Statement

Financial institutions process millions of transactions every day.

The primary challenge is identifying fraudulent transactions while minimizing false alarms.

An effective fraud detection system should:

* Detect as many frauds as possible.
* Reduce false positives.
* Maintain high Precision and Recall.
* Be explainable.
* Be deployable in production.

---

# 🎯 Objectives

The objectives of this project are:

* Detect fraudulent transactions using Machine Learning.
* Compare multiple classification algorithms.
* Address severe class imbalance.
* Optimize the best-performing model.
* Explain model predictions using SHAP.
* Optimize classification thresholds.
* Evaluate business cost trade-offs.
* Build a reusable prediction pipeline.
* Deploy the trained model through a REST API.

---

# 📊 Dataset

**Dataset:** Credit Card Fraud Detection Dataset

### Dataset Characteristics

* Total Transactions: **284,807**
* Fraud Cases: **492**
* Features: **30**
* Target Classes:

  * **0 → Legitimate Transaction**
  * **1 → Fraudulent Transaction**

The dataset is highly imbalanced, making model evaluation particularly challenging.

---

# 🔄 Project Workflow

```
Dataset
   │
   ▼
Exploratory Data Analysis
   │
   ▼
Data Preprocessing
   │
   ▼
Model Training
   │
   ▼
Model Comparison
   │
   ▼
Hyperparameter Tuning
   │
   ▼
Model Explainability (SHAP)
   │
   ▼
Threshold Optimization
   │
   ▼
Cost-sensitive Evaluation
   │
   ▼
Production Pipeline
   │
   ▼
FastAPI Deployment
```

---

# 📈 Exploratory Data Analysis

The exploratory analysis focused on:

* Class distribution
* Feature distributions
* Correlation analysis
* Transaction amount analysis
* Fraud pattern investigation

The analysis confirmed the severe imbalance between legitimate and fraudulent transactions.

---

# 🧹 Data Preprocessing

The preprocessing stage included:

* Train/Test Split
* Feature Scaling (where required)
* Data validation
* Pipeline integration

---

# 🤖 Machine Learning Models

The following models were trained and evaluated:

* Logistic Regression
* Multi-Layer Perceptron (MLP)
* Random Forest
* XGBoost
* LightGBM

Each model was evaluated using:

* Precision
* Recall
* F1-score
* ROC-AUC
* Average Precision Score

---

# 🏆 Model Selection

Following extensive experimentation, **XGBoost** demonstrated the best overall performance.

Reasons for selection include:

* High Recall
* Strong Precision
* Excellent ROC-AUC
* Robust Average Precision
* Stable decision boundary
* Good generalization capability

---

# ⚙️ Hyperparameter Optimization

Hyperparameter tuning was performed using Randomized Search Cross Validation.

Optimized parameters included:

* Number of Trees
* Learning Rate
* Maximum Tree Depth
* Minimum Child Weight
* Gamma
* Subsample Ratio
* Column Sampling

The tuned model achieved improved predictive performance compared to the default configuration.

---

# 🔍 Model Explainability

Model interpretability was performed using **SHAP (SHapley Additive Explanations)**.

The explainability analysis includes:

* SHAP Summary Plot
* Feature Importance
* Individual Prediction Explanation

This provides transparency into how the model makes fraud detection decisions.

---

# 🎯 Threshold Optimization

Rather than using the default probability threshold of **0.50**, multiple thresholds were evaluated.

The optimal threshold was selected based on the trade-off between:

* Precision
* Recall
* Business requirements

This significantly improved the operational usefulness of the model.

---

# 💰 Cost-sensitive Evaluation

A business-oriented evaluation was conducted by assigning different costs to:

* False Positives
* False Negatives

This approach reflects real-world fraud detection systems where missing a fraudulent transaction is generally much more expensive than investigating a legitimate one.

---

# 🔄 Production Pipeline

A reusable Scikit-Learn Pipeline was created to ensure consistent preprocessing and prediction.

Benefits include:

* Reproducibility
* Simplified inference
* Reduced preprocessing errors
* Easy deployment

The trained pipeline was serialized using Joblib.

---

# 🚀 FastAPI Deployment

The final model was deployed using **FastAPI**.

Implemented features:

* REST API
* JSON Input
* JSON Output
* Automatic Swagger Documentation
* Pydantic Validation
* Pipeline-based Prediction

---

# 📂 Project Structure

```text
Fraud_Detection/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── model.py
│   └── schemas.py
│
├── assets/
│
├── models/
│   └── fraud_detection_pipeline.pkl
│
├── notebooks/
│   └── Fraud_Detection.ipynb
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone <repository_url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the API

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# 📡 API Example

POST request:

```json
{
  "Time": 0,
  "V1": 0,
  "...": "...",
  "Amount": 149.62
}
```

Response:

```json
{
  "prediction": 0,
  "fraud_probability": 0.000005
}
```

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* LightGBM
* SHAP
* Matplotlib
* Seaborn
* FastAPI
* Pydantic
* Joblib

---

# 🔮 Future Improvements

Potential future enhancements include:

* Docker containerization
* Cloud deployment
* CI/CD pipeline
* Model monitoring
* Data drift detection
* Automatic model retraining
* Authentication for API endpoints

---

# 👩‍💻 Author

**Hediye**

Machine Learning & Data Science

---

⭐ If you found this project useful, consider giving it a star.
