from pydantic import BaseModel

class Transaction(BaseModel):

    amount: float
    location: str
    time: int
    age: int
    balance: float

class FraudResult(BaseModel):
    is_fraud: bool
    risk_score: float
    message: str