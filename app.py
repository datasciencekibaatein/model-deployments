import joblib
import numpy as np
from fastapi import FastAPI
from schema import BankNote

app = FastAPI(
    title="Bank note Aunthentication app",
    description="Predicts whether a banknote is authentic or forged",
    version='1.0.0'
)

model = joblib.load("model/classifier.joblib")

@app.get("/")
def home():
    return {"message":"Bank note authentication api is running"}

@app.get('/health')
def health():
    return {"status":"okk"}

@app.post("/predict")
def predict(note:BankNote):
    features = np.array([[note.variance,note.skewness,note.curtosis,note.entropy]])
    prediction = int(model.predict(features)[0])
    confidence = float(model.predict_proba(features)[0][prediction])
    label = "Forged note" if prediction == 1 else "Authentic note"
    return {"prediction":prediction, "label":label, "confidence":round(confidence,4)}