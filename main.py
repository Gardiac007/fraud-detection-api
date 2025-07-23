from fastapi import FastAPI, HTTPException
from models import Transaction, FraudResult
from detector import FraudDetector

app = FastAPI(title="Simple Fraud Detection API")

detector = FraudDetector()

@app.get("/")
def home():
    return {"message": "Fraud Detection API is running!"}

@app.post("/check-fraud", response_model=FraudResult)
def check_fraud(transaction: Transaction):
    
    is_fraud, risk_score, message = detector.check_transaction(transaction)

    return FraudResult(
        is_fraud=is_fraud,
        risk_score=risk_score,
        message=message
    )
    