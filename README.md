# 🕵️‍♂️ Fraud Detection API

A lightweight and efficient **Fraud Detection API** built with **FastAPI** and powered by a Machine Learning model.

---

## 🚀 Features

- ✅ Built with **FastAPI** for fast performance
- 🧠 Integrates a pre-trained **Machine Learning model**
- 📦 Exposes a **/predict** endpoint to detect fraud
- 🔒 Input validation using **Pydantic**
- 📊 Scalable and ready for real-world datasets

---

## 🧪 Example API Usage

**POST** `/check-fraud`

### 🔧 Request Body:
```json
{
  "amount": 129.99,
  "location": "domestic",
  "time": 14,
  "age": 20,
  "balance": 1000
}
```

### ✅ Sample Response:
```json
{
  "is_fraud": false,
  "risk_score": 0,
  "message": "LOW RISK: Transaction approved!"
}
```

---

## 📚 Tech Stack

- **FastAPI** — API framework
- **Scikit-learn** — ML backend
- **Pydantic** — Validation
- **Uvicorn** — ASGI server

---

## 📌 TODOs

- [ ] Add authentication (e.g., API key)
- [ ] Logging and monitoring
- [ ] Dockerize the project
- [ ] Deploy on cloud (Heroku, AWS, etc.)

---
