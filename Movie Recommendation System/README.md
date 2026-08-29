# 🎬 Movie Recommendation System

An end-to-end movie recommendation system built for a hypothetical movie streaming platform.

The project focuses on personalized recommendations using collaborative filtering and the Alternating Least Squares (ALS) algorithm. It covers the main stages of a recommendation workflow, from preparing user–movie interactions and training the model to evaluating recommendations and serving them through a REST API.

---

## 🎯 Project Goal

The main goal is to recommend movies that are relevant to each user based on their historical rating behavior.

Instead of relying only on movie genres or metadata, the system learns patterns from user–movie interactions and uses these patterns to identify movies that a user may be interested in.

---

## 📊 Dataset

The project uses the **MovieLens 25M** dataset.

The main data sources used in the recommendation pipeline are:

- `ratings.csv` — User–movie rating interactions.
- `movies.csv` — Movie titles and genres.

Additional movie metadata was also explored during the project for feature analysis and recommendation-related experiments.

---

## 🧠 Recommendation Approach

The recommendation engine uses **Collaborative Filtering** with the **Alternating Least Squares (ALS)** algorithm.

The rating data is transformed into a sparse user–item interaction matrix. ALS then learns latent representations for users and movies from these interactions.

The resulting model is used to generate personalized Top-K movie recommendations.

### Pipeline

```text
MovieLens Ratings
       ↓
Data Preparation
       ↓
User / Movie Index Mapping
       ↓
Sparse User–Item Matrix
       ↓
ALS Model Training
       ↓
Candidate Generation
       ↓
Filtering & Ranking
       ↓
Top-K Recommendations
       ↓
REST API
```
---

## 📈 Evaluation

The recommendation system was evaluated from several perspectives rather than relying on a single metric.

The evaluation included:

Recall@K — Measures how many relevant movies were successfully retrieved within the top K recommendations.
Catalog Coverage — Measures how much of the available movie catalog is recommended across users.
Intra-List Diversity — Measures how different the recommended movies are from one another within a recommendation list.

The system was evaluated using multiple recommendation sizes, including K = 5, 10, 20, and 50.

---

🔎 Example Recommendations

The trained model generates personalized recommendations for individual users.

For example, different users receive different movie lists based on their historical interaction patterns.

Example:
```text
User 1
────────────────────────────────────────
Three Colors: White
Shrek
Amores Perros
The Lord of the Rings: The Fellowship of the Ring
Monsters, Inc.
Eternal Sunshine of the Spotless Mind
```

The recommendation score is the model's ranking score and is used to order candidate movies; it should not be interpreted as a predicted rating on a 1–5 scale.

---

## 🌐 REST API

The trained recommendation system is exposed through a REST API built with FastAPI.

The API receives a user ID and the requested number of recommendations and returns ranked movie recommendations.

API implementation:

```text
api/
├── main.py
├── recommender.py
└── schemas.py
```
---

## 📁 Project Structure

```text
Movie Recommendation System/
│
├── api/
│   ├── main.py
│   ├── recommender.py
│   └── schemas.py
│
├── .gitignore
├── requirements.txt
├── Movie Recommendation System.ipynb
└── README.md
```
---

## 🛠️ Technologies

- Python
- Polars
- NumPy
- Scikit-learn
- Implicit
- FastAPI
- Pydantic
- Jupyter Notebook
- Git & GitHub
---

## 🚀 Future Improvements

Possible improvements include:

Building a hybrid recommender combining collaborative filtering with content-based features.
Handling the cold-start problem for new users and movies.
Adding more advanced ranking and re-ranking strategies.
Expanding offline evaluation with additional recommendation metrics.
Deploying the API to a cloud environment.

---

👤 Author

Hediye

Data Science / Machine Learning Portfolio Project