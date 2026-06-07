# 🚀 SpaceX Falcon 9 Launch Success Prediction

Machine Learning project for predicting the success of SpaceX Falcon 9 rocket launches using multiple classification algorithms.

---

## 🌌 Overview

SpaceX significantly reduced the cost of space missions through the reusability of Falcon 9 boosters. Predicting whether a launch will be successful is an interesting machine learning classification problem with real-world relevance.

In this project, multiple supervised learning algorithms are trained and compared to predict Falcon 9 mission outcomes based on launch-related features.

---

## 🎯 Objective

Build a machine learning model capable of predicting whether a Falcon 9 launch will be successful.

### Target Variable

```text
1 → Successful Launch
0 → Failed Launch
```

---

## 🔍 Project Workflow

### 📊 Exploratory Data Analysis

Initial analysis includes:

- Dataset inspection
- Statistical summaries
- Feature exploration
- Correlation analysis
- Data visualization

---

### 🧹 Data Preprocessing

Data preparation steps:

- Feature selection
- Data cleaning
- Handling categorical variables
- Feature scaling
- Train/Test split

---

### 🤖 Machine Learning Models

Several classification algorithms were trained and evaluated.

#### 📈 Logistic Regression

A strong baseline linear classifier.

#### 🎯 Support Vector Machine (SVM)

Margin-based classification algorithm.

#### 🌳 Decision Tree

Interpretable tree-based learning model.

#### 👥 K-Nearest Neighbors (KNN)

Distance-based classification approach.

---

## ⚙️ Hyperparameter Optimization

Grid Search Cross Validation was used to identify optimal model configurations.

```python
GridSearchCV()
```

This helps improve model performance while reducing manual tuning.

---

## 📏 Model Evaluation

Models were evaluated using:

- Accuracy Score
- Classification Report
- Confusion Matrix
- ROC Curve Analysis

```python
classification_report()
confusion_matrix()
RocCurveDisplay()
```

---

## 🏆 Model Comparison

The project compares the performance of multiple machine learning algorithms to determine which model performs best on the Falcon 9 launch dataset.

```text
Logistic Regression
Support Vector Machine
Decision Tree
K-Nearest Neighbors
```

Performance metrics are collected and ranked for comparison.

---

## 🛠 Tech Stack

<p align="left">

🐍 Python  
📊 Pandas  
🔢 NumPy  
📉 Matplotlib  
🎨 Seaborn  
🤖 Scikit-Learn

</p>

---

## 📂 Project Structure

```text
├── All Models Machine Learning for Space X Falcon 9.ipynb
├── dataset.csv
├── README.md
```

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/your-username/spacex-falcon9-launch-prediction.git
```

### Install Requirements

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Run Notebook

```bash
jupyter notebook
```

---

## 📚 Key Concepts Demonstrated

✅ Binary Classification

✅ Data Preprocessing

✅ Feature Scaling

✅ Hyperparameter Tuning

✅ Model Comparison

✅ Performance Evaluation

✅ ROC Analysis

---

## 🔭 Future Improvements

Potential extensions include:

- Random Forest Classifier
- XGBoost
- LightGBM
- Ensemble Learning
- Feature Importance Analysis
- Deployment with FastAPI
- Interactive Dashboard

---

## 📝 Project Background

This repository represents one of my early machine learning projects and reflects my learning journey in predictive analytics and classification modeling.

The primary focus was understanding how different machine learning algorithms behave on the same real-world dataset and comparing their predictive performance.

---

### ⭐ If you find this project interesting, feel free to star the repository.
