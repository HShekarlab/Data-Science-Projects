# 🧠 Customer Segmentation using RFM Analysis & KMeans Clustering

An end-to-end customer segmentation project that combines traditional RFM analysis with unsupervised machine learning techniques to identify meaningful customer groups and generate actionable business insights.

---

## 🎯 Project Objective

Understanding customer behavior is one of the most important challenges in data-driven businesses.

The goal of this project is to:

- Analyze customer purchasing behavior
- Build RFM-based customer profiles
- Segment customers using both rule-based and machine learning approaches
- Compare segmentation strategies
- Translate analytical findings into business recommendations

---

## 📊 Dataset

This project uses the **Online Retail Dataset** containing transactional records from a UK-based online retailer.

The dataset includes:

- Invoice information
- Product details
- Purchase quantities
- Transaction dates
- Customer identifiers
- Product prices

---

## 🔄 Project Workflow

### 1️⃣ Data Cleaning & Preparation

- Removed cancelled transactions
- Removed invalid quantities and prices
- Handled missing values
- Converted columns to appropriate data types

---

### 2️⃣ Exploratory Data Analysis (EDA)

Performed exploratory analysis to understand:

- Transaction distribution
- Purchase quantities
- Product pricing behavior
- Customer activity patterns
- Outlier detection using boxplots

Several distributions were analyzed using both standard and log-transformed visualizations.

---

### 3️⃣ RFM Feature Engineering

Built three core behavioral metrics:

| Metric | Description |
|----------|-------------|
| Recency | Days since last purchase |
| Frequency | Number of purchases |
| Monetary | Total spending |

These features summarize customer purchasing behavior.

---

### 4️⃣ Rule-Based Customer Segmentation

Customers were scored using quantile-based RFM scoring and assigned to business-friendly segments such as:

- Champions
- Loyal Customers
- Potential Loyalists
- At Risk
- Lost Customers

---

### 5️⃣ Customer Clustering (KMeans)

Applied unsupervised machine learning to discover hidden customer structures.

#### Preprocessing

- Log Transformation
- Standard Scaling

#### Model Selection

The optimal number of clusters was determined using the **Elbow Method**.

#### Final Model

- Algorithm: KMeans
- Number of Clusters: 4

---

### 6️⃣ Cluster Validation & Visualization

To evaluate cluster quality:

- Elbow Method was used
- PCA dimensionality reduction was applied
- Cluster separation was visualized in 2D space

---

### 7️⃣ Cluster Interpretation

The final clusters were interpreted as:

| Cluster | Description |
|-----------|------------|
| 🟢 High Value | Recent, frequent, high-spending customers |
| 🟡 Mid Value | Active customers with growth potential |
| 🔵 Occasional | Low-frequency recent customers |
| 🔴 Lost | Inactive and low-value customers |

---

## 💼 Business Recommendations

### High Value Customers
- Loyalty programs
- Premium offers
- VIP campaigns

### Mid Value Customers
- Upselling opportunities
- Personalized recommendations

### Occasional Customers
- Engagement campaigns
- Repeat purchase incentives

### Lost Customers
- Reactivation campaigns
- Win-back promotions

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn

---

## 📈 Key Takeaways

This project demonstrates:

- Data cleaning and preprocessing
- Exploratory data analysis
- Feature engineering
- Customer analytics
- Unsupervised machine learning
- Cluster interpretation
- Business-driven decision making

---

## 🚀 Future Improvements

Potential enhancements include:

- Silhouette Score evaluation
- Additional clustering algorithms
- Customer Lifetime Value (CLV) modeling
- Churn prediction models
- Interactive dashboards

---

## 📂 Repository Structure

```text
├── Customer Segmentation (RFM + Clustering).ipynb
├── README.md
└── images/
```

---

## ⭐ Conclusion

By combining classical RFM analysis with machine learning-based clustering, this project provides a practical framework for understanding customer behavior and supporting data-driven marketing strategies.
