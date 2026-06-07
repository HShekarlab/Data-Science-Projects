# 🩺 Diabetes Prediction using Machine Learning

A machine learning project for predicting diabetes diagnosis based on medical diagnostic measurements.

---

## Overview

Early detection of diabetes can significantly improve treatment outcomes and reduce long-term health complications.

This project explores a structured healthcare dataset and applies multiple machine learning algorithms to classify whether a patient is diabetic or non-diabetic based on clinical attributes.

The project covers the complete machine learning workflow:

- Data Exploration
- Feature Analysis
- Data Preprocessing
- Feature Scaling
- Model Training
- Model Comparison
- Patient-Level Prediction

---

## Problem Statement

The objective is to build a binary classification model capable of predicting diabetes status from patient medical records.

Target Variable:

```text
Outcome
0 → Non-Diabetic
1 → Diabetic
```

---

## Dataset Features

The dataset contains several medical measurements commonly used in diabetes screening.

| Feature | Description |
|----------|------------|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Triceps skin fold thickness |
| Insulin | 2-Hour serum insulin |
| BMI | Body Mass Index |
| DiabetesPedigreeFunction | Diabetes hereditary score |
| Age | Patient age |
| Outcome | Diabetes diagnosis |

---

## Project Workflow

### Data Exploration

Performed initial analysis using:

- Dataset inspection
- Descriptive statistics
- Missing value checking
- Class-wise aggregation

```python
df.describe()
df.info()
df.groupby("Outcome").mean()
```

---

### Exploratory Data Analysis

Visualization techniques used:

- Pairplots
- Feature relationship analysis
- Distribution exploration

```python
sns.pairplot(df)
```

These visualizations help identify patterns associated with diabetes diagnosis.

---

### Data Preprocessing

Features and target were separated:

```python
X = df.drop("Outcome", axis=1)
y = df["Outcome"]
```

Standardization was applied using:

```python
StandardScaler()
```

to ensure all variables contribute equally during model training.

---

## Machine Learning Models

Several classification algorithms were evaluated.

### Logistic Regression

```text
Baseline Linear Classifier
```

### Support Vector Machine (SVM)

```text
Margin-Based Classification
```

### Decision Tree

```text
Tree-Based Classification
```

### Random Forest

```text
Ensemble Learning
```

### K-Nearest Neighbors (KNN)

```text
Distance-Based Classification
```

### LazyPredict Benchmarking

The project also uses LazyPredict to automatically compare multiple machine learning models and rank their performance.

---

## Model Evaluation

Performance was evaluated using test accuracy scores generated after train-test splitting.

```python
train_test_split(
    test_size=0.25,
    random_state=75
)
```

The goal was to compare different algorithms and identify the most suitable classifier for the dataset.

---

## Patient Prediction Example

The final workflow includes predicting diabetes status for a new patient:

```python
prediction = model.predict(new_patient_data)
```

Output:

```text
The person is diabetic
```

or

```text
The person is not diabetic
```

---

## Tech Stack

<div>

Python • Pandas • NumPy • Seaborn • Scikit-Learn • LazyPredict

</div>

---

## Project Structure

```text
├── Diabetes.ipynb
├── diabetes.csv
├── README.md
```

---

## Installation

```bash
pip install pandas numpy seaborn scikit-learn lazypredict
```

---

## Run the Project

```bash
jupyter notebook
```

Open:

```text
Diabetes.ipynb
```

and run all cells sequentially.

---

## Key Learnings

This project helped strengthen understanding of:

- Binary Classification
- Healthcare Data Analysis
- Feature Scaling
- Model Evaluation
- Classical Machine Learning Algorithms
- Comparing Multiple Models

---

## Future Improvements

Potential enhancements include:

- Hyperparameter Optimization
- Cross Validation
- Feature Selection
- ROC-AUC Analysis
- Explainability with SHAP
- Model Deployment using FastAPI

---

## Notes

This repository represents one of my early machine learning projects and documents my learning journey in applied Data Science and predictive healthcare analytics.

⭐ Feel free to explore, fork, or improve the project.
