# 🚢 Titanic Survival Prediction

Machine Learning project focused on predicting passenger survival aboard the RMS Titanic using demographic and travel-related information.

---

## 📖 Overview

The sinking of the Titanic remains one of the most well-known maritime disasters in history.

This project explores passenger data to identify patterns associated with survival and builds predictive machine learning models capable of estimating whether a passenger would survive the disaster.

The project follows a complete machine learning workflow:

- Data Exploration
- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Model Training
- Model Evaluation
- Survival Prediction

---

## 🎯 Objective

Develop a binary classification model that predicts passenger survival based on personal and travel characteristics.

### Target Variable

```text
Survived

0 → Did Not Survive
1 → Survived
```

---

## 📊 Dataset Features

| Feature | Description |
|----------|------------|
| PassengerId | Unique passenger identifier |
| Pclass | Ticket class |
| Name | Passenger name |
| Sex | Gender |
| Age | Passenger age |
| SibSp | Number of siblings/spouses aboard |
| Parch | Number of parents/children aboard |
| Ticket | Ticket number |
| Fare | Passenger fare |
| Cabin | Cabin number |
| Embarked | Port of embarkation |
| Survived | Target variable |

---

## 🔍 Exploratory Data Analysis

Several visual analyses were performed to understand the dataset:

### 📈 Distribution Analysis

- Passenger Class Distribution
- Gender Distribution
- Age Distribution
- Fare Distribution

### 🎨 Relationship Analysis

- Survival vs Gender
- Survival vs Passenger Class
- Survival vs Age
- Survival vs Fare

### 🔥 Correlation Analysis

- Correlation Heatmaps
- Feature Relationships
- Survival Drivers

These visualizations help uncover factors that influenced passenger survival.

---

## 🧹 Data Preprocessing

### Missing Value Handling

Missing values were identified and treated appropriately.

### Categorical Encoding

Categorical variables such as:

```text
Sex
Embarked
```

were transformed into numerical representations.

### Feature Selection

Relevant features were selected for model training while removing non-informative columns.

### Feature Scaling

Numerical features were standardized to improve model performance.

---

## 🤖 Machine Learning Models

Multiple classification algorithms were explored and compared.

### 📈 Logistic Regression

Linear probabilistic classification model.

### 🌲 Decision Tree

Interpretable rule-based classifier.

### 🌳 Random Forest

Ensemble learning approach using multiple decision trees.

### 🎯 Support Vector Machine (SVM)

Margin-based classification algorithm.

### 👥 K-Nearest Neighbors (KNN)

Distance-based classifier.

---

## 📏 Evaluation Metrics

Models were evaluated using:

- Accuracy Score
- Confusion Matrix
- Classification Report
- Cross Validation

```python
accuracy_score()
classification_report()
confusion_matrix()
```

---

## 🏆 Key Insights

Some notable findings from the analysis:

✅ Female passengers had significantly higher survival rates.

✅ First-class passengers were more likely to survive.

✅ Passenger age showed a relationship with survival probability.

✅ Ticket class and fare were among the most influential features.

---

## 🛠 Tech Stack

<div align="left">

🐍 Python

📊 Pandas

🔢 NumPy

📉 Matplotlib

🎨 Seaborn

🤖 Scikit-Learn

📓 Jupyter Notebook

</div>

---

## 📂 Project Structure

```text
├── Titanic.ipynb
├── train.csv
├── README.md
```

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/your-username/titanic-survival-prediction.git
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
Titanic.ipynb
```

and execute all notebook cells.

---

## 📚 Skills Demonstrated

✔ Exploratory Data Analysis (EDA)

✔ Data Cleaning

✔ Missing Value Treatment

✔ Feature Engineering

✔ Classification Modeling

✔ Model Evaluation

✔ Predictive Analytics

---

## 🔮 Future Improvements

Potential enhancements include:

- XGBoost Implementation
- LightGBM Comparison
- Hyperparameter Optimization
- Feature Importance Analysis
- SHAP Explainability
- Interactive Dashboard
- Model Deployment with FastAPI

---

## 🌟 Learning Journey

This repository represents one of my early machine learning projects and showcases foundational concepts in classification, feature engineering, and predictive analytics.

While simple by today's standards, it played an important role in developing practical machine learning skills and understanding real-world data workflows.

---

### ⭐ Feel free to fork, explore, or contribute to the project.
