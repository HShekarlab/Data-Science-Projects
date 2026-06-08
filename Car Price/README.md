# 🚗 Car Price Prediction with Deep Learning

Predicting used car prices using exploratory data analysis, feature engineering, and Artificial Neural Networks (ANN).

---

## 📌 Project Overview

This project explores the relationship between vehicle specifications and market prices in order to build a regression model capable of estimating used car values.

The workflow covers the complete machine learning pipeline:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing
- Deep Learning Regression
- Model Evaluation

Although this was one of my early Data Science projects, it demonstrates the foundations of building end-to-end predictive models using structured tabular data.

---

## 🎯 Problem Statement

Used car pricing depends on multiple factors such as:

- Vehicle age
- Fuel type
- Transmission
- Ownership history
- Distance driven

The goal is to learn these relationships and predict the selling price of a vehicle using a neural network model.

---

## 📊 Dataset Features

| Feature | Description |
|----------|------------|
| Year | Manufacturing year |
| Selling Price | Target variable |
| KM Driven | Total kilometers driven |
| Fuel | Fuel type |
| Seller Type | Individual / Dealer |
| Transmission | Manual / Automatic |
| Owner | Ownership history |

---

## ⚙️ Data Processing Pipeline

### Data Cleaning

- Removed irrelevant columns
- Checked missing values
- Removed duplicate records

### Feature Engineering

Created a new feature:

```python
Age = CurrentYear - ManufacturingYear
```

This provides a more meaningful representation than raw manufacturing year.

### Encoding

Categorical variables were transformed into numerical representations suitable for model training.

### Scaling

Features were standardized using:

```python
StandardScaler()
```

to improve neural network convergence.

---

## 📈 Exploratory Data Analysis

The project includes:

- Correlation Heatmaps
- Pairplots
- Distribution Analysis
- Missing Value Visualization
- Category Distribution Charts

These analyses helped identify important relationships between vehicle characteristics and selling prices.

---

## 🧠 Deep Learning Model

A fully connected Artificial Neural Network (ANN) was implemented using TensorFlow/Keras.

### Architecture

```text
Input Layer
     ↓
Dense(40) + ReLU
     ↓
Dense(35) + ReLU
     ↓
Dense(30) + ReLU
     ↓
Dense(25) + ReLU
     ↓
Dense(20) + ReLU
     ↓
Dense(15) + ReLU
     ↓
Dense(10) + ReLU
     ↓
Output Layer (Price)
```

### Training Configuration

| Parameter | Value |
|------------|--------|
| Optimizer | RMSprop |
| Loss Function | MSE |
| Epochs | 200 |
| Task | Regression |

---

## 📏 Evaluation Metrics

Model performance was evaluated using:

- Mean Squared Error (MSE)
- R² Score

Predictions were generated for both training and testing datasets to assess generalization capability.

---

## 🛠 Tech Stack

<p>
Python • Pandas • NumPy • Matplotlib • Seaborn • Scikit-Learn • TensorFlow • Keras
</p>

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/your-username/car-price-prediction.git
```

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn tensorflow
```

### Run

Open the notebook and execute all cells:

```bash
jupyter notebook
```

---

## 📂 Project Structure

```text
├── Car Price.ipynb
├── dataset.csv
├── README.md
```

---

## 🔍 Key Learnings

This project helped reinforce several core Data Science concepts:

- Data preprocessing for tabular datasets
- Feature engineering techniques
- Neural network implementation for regression
- Model evaluation and validation
- End-to-end machine learning workflows

---

## 📌 Future Improvements

Potential improvements include:

- XGBoost comparison
- LightGBM benchmarking
- Hyperparameter tuning
- Cross-validation
- Feature importance analysis
- Model deployment with FastAPI

---

## 👨‍💻 About

This repository represents one of my early deep learning projects and reflects my progression in Data Science and Machine Learning engineering.

If you find this project useful, feel free to ⭐ the repository.
