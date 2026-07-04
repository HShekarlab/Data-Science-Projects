import joblib

from app.config import MODEL_PATH

# ==================================================
# Load trained pipeline
# ==================================================

pipeline = joblib.load(MODEL_PATH)


# ==================================================
# Prediction Function
# ==================================================

def predict_transaction(data):

    prediction = pipeline.predict(data)[0]

    probability = pipeline.predict_proba(data)[0][1]

    return prediction, probability