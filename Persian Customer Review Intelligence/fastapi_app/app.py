from pathlib import Path

import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from hazm import Normalizer


# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_DIR = BASE_DIR / "models" / "sentiment_api"

MODEL_PATH = MODEL_DIR / "sentiment_model.joblib"
VECTORIZER_PATH = MODEL_DIR / "tfidf_vectorizer.joblib"


# --------------------------------------------------
# Load model artifacts
# --------------------------------------------------

model = joblib.load(MODEL_PATH)

tfidf_vectorizer = joblib.load(VECTORIZER_PATH)


# --------------------------------------------------
# Persian text normalizer
# --------------------------------------------------

normalizer = Normalizer(
    correct_spacing=True,
    remove_diacritics=True,
    remove_specials_chars=True,
    decrease_repeated_chars=False,
    persian_style=True,
    persian_numbers=False,
    unicodes_replacement=True,
    seperate_mi=True,
)


# --------------------------------------------------
# FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="Persian Customer Review Sentiment API",
    description="A REST API for Persian customer review sentiment classification.",
    version="1.0.0",
)


# --------------------------------------------------
# Request schema
# --------------------------------------------------

class ReviewRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="Persian customer review text"
    )


# --------------------------------------------------
# Prediction function
# --------------------------------------------------

def predict_sentiment(text: str) -> dict:
    processed_text = normalizer.normalize(text).strip()

    if not processed_text:
        raise ValueError(
            "The input review is empty after preprocessing."
        )

    text_tfidf = tfidf_vectorizer.transform(
        [processed_text]
    )

    predicted_label = model.predict(
        text_tfidf
    )[0]

    sad_probability = model.predict_proba(
        text_tfidf
    )[0, 1]

    confidence = (
        sad_probability
        if predicted_label == "SAD"
        else 1 - sad_probability
    )

    return {
        "sentiment": predicted_label,
        "confidence": round(float(confidence), 4),
        "sad_probability": round(float(sad_probability), 4),
    }


# --------------------------------------------------
# Health check
# --------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "Persian Customer Review Sentiment API is running."
    }


# --------------------------------------------------
# Prediction endpoint
# --------------------------------------------------

@app.post("/predict")
def predict(request: ReviewRequest):
    try:
        return predict_sentiment(request.text)

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

# --------------------------------------------------
# Health endpoint
# --------------------------------------------------

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "vectorizer_loaded": tfidf_vectorizer is not None
    }