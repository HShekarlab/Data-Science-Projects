from fastapi import FastAPI, HTTPException
import pandas as pd

from app.schemas import Transaction, PredictionResponse
from app.model import predict_transaction

app = FastAPI()


# ==================================================
# Home Endpoint
# ==================================================

@app.get("/")
def home():
    return {
        "message": "Fraud Detection API is running"
    }


# ==================================================
# Prediction Endpoint
# ==================================================

@app.post("/predict", response_model=PredictionResponse)
def predict(transaction: Transaction):

    try:

        # Convert request to DataFrame
        data = pd.DataFrame([transaction.model_dump()])

        # Prediction
        prediction, probability = predict_transaction(data)

        # Response
        return PredictionResponse(
            prediction=int(prediction),
            fraud_probability=float(probability)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )