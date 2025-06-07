# Clustering Asian Currencies Based on Exchange Rate Behaviors

This project explores the behavior of different Asian currencies against the US Dollar (USD) and applies clustering techniques to group currencies with similar exchange rate patterns.

## 📌 Overview

- **Goal:** Identify and visualize similarities in exchange rate behaviors of different currencies.
- **Approach:** 
  - Data cleaning and preprocessing
  - Exploratory data analysis
  - Handling missing values
  - Correlation analysis
  - KMeans clustering
  - Visualizing currency clusters

## 🧰 Technologies Used

- Python (Pandas, NumPy, Scikit-learn, Plotly, Seaborn, Matplotlib)
- Jupyter Notebook

## 📈 Dataset

- Source: A historical dataset containing daily exchange rates of multiple currencies against the USD.
- Includes currencies from various countries (e.g., Japan, Korea, etc.).
- Timeframe and structure can be found in the notebook.

## 🔍 Key Highlights

- NaN values handled using forward fill strategy
- Returns calculated using log-difference of exchange rates
- Currencies grouped using KMeans clustering (based on return behavior)
- Interactive and color-coded visualization of clusters with Plotly
- Clear summary of which currencies belong to which cluster


## 📁 Files

- `Clustering Asian currencies based on exchange rate behaviors.ipynb`: The full Jupyter Notebook with code, analysis, and visualizations.
- `Dollar-Exchange.csv`: Raw exchange rate data.
- `README.md`: Project description.

## 🚀 How to Run

1. Clone the repository
2. Make sure the CSV file is in the same directory as the notebook
3. Run the notebook in Jupyter or any Python environment
