# Persian Customer Review Intelligence

An end-to-end Persian sentiment analysis project for customer reviews, covering data preparation, Persian text normalization, classical machine learning, error analysis, model export, and REST API deployment.

---

## Overview

Customer reviews contain valuable information about user satisfaction, service quality, delivery performance, and overall customer experience.

The goal of this project is to build a practical sentiment classification system for Persian customer reviews and classify each review into one of two sentiment classes:

- **HAPPY**
- **SAD**

The project follows a complete machine learning workflow, from raw review data and text preprocessing to model evaluation and API deployment.

---

## Project Objectives

The main objectives of this project are to:

- Analyze and validate Persian customer review data
- Apply Persian-specific text normalization
- Detect and remove cross-split data leakage
- Build a strong TF-IDF baseline
- Compare multiple machine learning approaches
- Evaluate the feasibility of a Persian BERT-based approach
- Analyze model errors and high-confidence misclassifications
- Train the final model on the combined training and validation data
- Evaluate the final model on an isolated test set
- Export the trained model for reuse
- Serve predictions through a FastAPI REST API

---

## Dataset

The project uses a Persian customer review dataset containing separate training, validation, and test splits.

After leakage cleanup, the datasets contained:

| Split | Samples |
|---|---:|
| Train | 52,110 |
| Validation | 8,334 |
| Test | 9,030 |

The final training stage combined the training and validation sets:

| Final Training Data | Samples |
|---|---:|
| Train + Validation | 60,444 |

The target variable contains two classes:

- `HAPPY`
- `SAD`

---

## Project Workflow

```text
Raw Reviews
     ↓
Data Audit
     ↓
Persian Text Normalization
     ↓
Duplicate & Leakage Detection
     ↓
TF-IDF Feature Extraction
     ↓
Model Comparison
     ↓
Final Model Selection
     ↓
Error Analysis
     ↓
Final Training
     ↓
Independent Test Evaluation
     ↓
Inference Pipeline
     ↓
Model Export
     ↓
FastAPI Deployment
````

---

## 1. Data Audit

The initial dataset was examined for:

* Dataset dimensions
* Column types
* Missing values
* Class distribution
* Duplicate reviews
* English characters
* Digits
* URLs
* Arabic characters
* Zero-width non-joiners
* Repeated characters
* Other text normalization issues

This stage was used to identify data-quality issues before modeling.

---

## 2. Persian Text Normalization

Persian text requires specific preprocessing because real-world user-generated content often contains inconsistent Unicode representations, Arabic/Persian character variants, spacing issues, and repeated characters.

The preprocessing pipeline included normalization of:

* Arabic/Persian character variants
* Unicode representations
* Spacing
* Diacritics
* Persian text formatting
* Other normalization inconsistencies

The preprocessing step was applied consistently to the data used for modeling and later inference.

---

## 3. Data Leakage Prevention

Potential overlap between train, validation, and test sets was explicitly checked.

Before cleanup, duplicate review overlaps existed between:

* Train and Validation
* Train and Test

These overlapping samples were removed from the validation and test sets.

After cleanup:

```text
Train ↔ Validation = 0 overlaps
Train ↔ Test       = 0 overlaps
Validation ↔ Test  = 0 overlaps
```

No conflicting duplicate labels remained across the cleaned splits.

This step ensured that the final test evaluation was performed on unseen reviews.

---

## 4. TF-IDF Baseline

TF-IDF was used as the main text representation for the classical machine learning pipeline.

The initial training representation contained:

* **52,110 reviews**
* **84,230 TF-IDF features**

The final training stage, after combining training and validation data, produced:

* **60,444 reviews**
* **94,570 TF-IDF features**

TF-IDF was selected as the main representation because it provides an efficient and interpretable way to represent textual information for linear classifiers.

---

## 5. Model Comparison

Several classical approaches were evaluated using the same validation data.

The main evaluation metrics were:

* Accuracy
* Precision for the SAD class
* Recall for the SAD class
* F1-score for the SAD class
* Macro F1

The final comparison showed that the evaluated classical models produced similar overall performance, while Logistic Regression provided a strong combination of predictive performance, computational efficiency, and interpretability.

---

## 6. Transformer Feasibility Assessment

A Persian BERT model, `HooshvareLab/bert-fa-base-uncased`, was also investigated as a potential deep learning approach.

Token-length analysis showed that most reviews were relatively short:

| Statistic       | Token Length |
| --------------- | -----------: |
| Minimum         |            4 |
| 50th percentile |           17 |
| 75th percentile |           28 |
| 90th percentile |           44 |
| 95th percentile |           57 |
| 99th percentile |           90 |
| Maximum         |          395 |

A maximum sequence length of 128 covered the vast majority of reviews, with only 120 reviews exceeding that limit.

However, full Transformer fine-tuning was not used as the final production approach because of the computational limitations of the available CPU-based environment.

This feasibility assessment helped establish the practical trade-off between model complexity and available computational resources.

---

## 7. Final Model

The final selected model is:

**TF-IDF + Logistic Regression**

The final model was retrained using the combined training and validation data:

* **Training samples:** 60,444
* **TF-IDF features:** 94,570

The final model completed training after 35 iterations.

---

## 8. Final Test Results

The final model was evaluated on the isolated test set containing 9,030 reviews.

| Metric          | Test Score |
| --------------- | ---------: |
| Accuracy        |     0.8607 |
| Precision (SAD) |     0.8354 |
| Recall (SAD)    |     0.9008 |
| F1 (SAD)        |     0.8669 |
| Macro F1        |     0.8604 |

### Classification Report

| Class | Precision | Recall | F1-score |
| ----- | --------: | -----: | -------: |
| HAPPY |      0.89 |   0.82 |     0.85 |
| SAD   |      0.84 |   0.90 |     0.87 |

### Confusion Matrix

```text
              Predicted
              HAPPY   SAD

Actual HAPPY   3676   807
Actual SAD      451  4096
```

The final test performance remained close to the validation performance, indicating consistent behavior on unseen data.

---

## 9. Error Analysis

Error analysis was performed to better understand the model's limitations.

The analysis included:

* Confusion matrix inspection
* High-confidence False Positives
* High-confidence False Negatives
* Review-length analysis
* Contrastive-expression analysis
* Examination of individual misclassified reviews

There were:

* **High-confidence False Positives:** 73
* **High-confidence False Negatives:** 25
* **Total high-confidence errors:** 98

The analysis suggested that the main challenges were associated with:

* Contrastive expressions
* Mixed sentiment
* Context-dependent sentiment
* Individual lexical cues that conflict with the overall meaning
* Potential annotation inconsistency in some reviews

Review length did not appear to be a major source of classification error, as error rates remained relatively similar across different length groups.

---

## 10. Contrastive Expression Analysis

Expressions such as:

* `ولی`
* `اما`
* `متاسفانه`

were specifically investigated because they can change or qualify the sentiment expressed in a sentence.

The analysis showed that reviews containing these expressions could have higher error rates than the overall validation error rate.

This provides a practical example of a limitation of lexical models: TF-IDF + Logistic Regression can capture strong word-level associations but does not explicitly model the contextual relationship between different parts of a sentence.

---

## 11. Inference Pipeline

A reusable inference pipeline was created for classifying unseen Persian reviews.

The inference process is:

```text
New Review
    ↓
Persian Text Normalization
    ↓
Fitted TF-IDF Vectorizer
    ↓
Logistic Regression
    ↓
Sentiment + Probability
```

### Example

**Review:**

```text
غذا خیلی خوشمزه بود و خیلی سریع به دستم رسید
```

**Prediction:**

```text
HAPPY
```

**SAD Probability:**

```text
0.0029
```

**Confidence:**

```text
0.9971
```

---

## 12. Model Export

The final trained model and fitted TF-IDF vectorizer were exported using `joblib`.

```text
models/
└── sentiment_api/
    ├── sentiment_model.joblib
    └── tfidf_vectorizer.joblib
```

This allows the trained system to be loaded independently from the Jupyter Notebook.

---

## 13. FastAPI Deployment

The trained model was exposed through a lightweight REST API using FastAPI.

The API provides:

### Health Check

**Endpoint:**

```text
GET /health
```

**Example response:**

```json
{
  "status": "healthy",
  "model_loaded": true,
  "vectorizer_loaded": true
}
```

### Sentiment Prediction

**Endpoint:**

```text
POST /predict
```

**Example request:**

```json
{
  "text": "غذا خیلی خوشمزه بود و سریع رسید"
}
```

**Example response:**

```json
{
  "sentiment": "HAPPY",
  "confidence": 0.9971,
  "sad_probability": 0.0029
}
```

The API also provides automatically generated interactive documentation through Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## 14. Project Structure

```text
p_15_Persian Customer Review Intelligence/
│
├── notebook.ipynb
├── README.md
├── .gitignore
│
├── models/
│   └── sentiment_api/
│       ├── sentiment_model.joblib
│       └── tfidf_vectorizer.joblib
│
└── fastapi_app/
    ├── app.py
    ├── test_api.py
    └── requirements.txt
```

---

## 15. Technologies

### Programming & Data Processing

* Python
* pandas
* NumPy
* scikit-learn

### Natural Language Processing

* Persian text normalization
* TF-IDF
* ParsBERT feasibility assessment

### Machine Learning

* Logistic Regression
* Classical ML model comparison
* Evaluation and error analysis

### Deployment

* FastAPI
* Uvicorn
* Pydantic
* Joblib
* REST API
* Swagger UI

---

## 16. Limitations

The final system has several limitations.

### Contextual Understanding

The TF-IDF + Logistic Regression approach is primarily lexical and does not explicitly model sentence-level context.

This can make contrastive and mixed-sentiment reviews more difficult to classify.

### Dataset Labels

Some high-confidence errors may reflect ambiguity or potential annotation inconsistency in the original dataset. These cases were analyzed but not manually relabeled.

### Transformer Deployment

A Persian BERT-based approach was investigated, but full fine-tuning was not adopted for the final system because of the computational limitations of the available CPU environment.

### Binary Sentiment Classification

The current system distinguishes only between HAPPY and SAD and does not provide finer-grained sentiment categories or aspect-level sentiment.

---

## 17. Future Improvements

Potential extensions include:

* Fine-tuning a Persian Transformer model on a GPU-enabled environment
* Aspect-based sentiment analysis
* Multi-class sentiment classification
* More advanced handling of contrastive and mixed-sentiment reviews
* Model monitoring after deployment
* Batch prediction endpoints
* Containerized deployment
* Cloud deployment
* A lightweight user interface for real-time predictions

---

## Conclusion

This project demonstrates a complete machine learning workflow for Persian sentiment analysis, from raw customer reviews and Persian-specific preprocessing to model evaluation, error analysis, model export, and REST API deployment.

The final TF-IDF + Logistic Regression system provides a practical and interpretable baseline with **86.04% Macro F1** on the held-out test set, while the error analysis identifies specific areas where contextual modeling could provide further improvements.

The project also demonstrates how a trained NLP model can be transformed from an experimental Jupyter Notebook workflow into a reusable prediction service through FastAPI.
