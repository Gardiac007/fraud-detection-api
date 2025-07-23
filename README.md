# 🕵️‍♂️ Fraud Detection API

A lightweight and efficient **Fraud Detection API** built with **FastAPI** and powered by a Machine Learning model. This project is designed to detect fraudulent transactions in real-time using trained ML models and is easily extendable for production use.

---

## 🚀 Features

- ✅ Built with **FastAPI** for blazing-fast performance
- 🧠 Integrates a pre-trained **Machine Learning model**
- 📦 Exposes a **/predict** endpoint to detect fraud
- 🔒 Input validation using **Pydantic**
- 📊 Scalable and ready for real-world datasets

---

## 📁 Project Structure

```
.
├── app/
│   ├── main.py               # FastAPI app with endpoints
│   ├── model.py              # ML model loading and prediction logic
│   ├── schemas.py            # Pydantic models for request/response
│   └── utils.py              # Helper functions (if any)
├── model/
│   └── fraud_model.pkl       # Trained ML model
├── requirements.txt
└── README.md
```

---

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/fraud-detection-api.git
cd fraud-detection-api
```

2. **Create virtual environment and install dependencies:**

```bash
python -m venv venv
source venv/bin/activate     # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

3. **Run the API locally:**

```bash
uvicorn app.main:app --reload
```

By default, it will be available at:  
📍 `http://127.0.0.1:8000`

---

## 🧪 Example API Usage

**POST** `/predict`

### 🔧 Request Body:
```json
{
  "amount": 129.99,
  "transaction_type": "online",
  "user_age": 34,
  "location": "US",
  "device_trusted": false
}
```

### ✅ Sample Response:
```json
{
  "is_fraud": true,
  "confidence": 0.87
}
```

---

## 🛠️ Train Your Own Model

If you want to train your own model on a different dataset:

```bash
# Inside a separate script or notebook
from sklearn.ensemble import RandomForestClassifier
# Train and save model as fraud_model.pkl
```

---

## 📚 Tech Stack

- **FastAPI** — API framework
- **Scikit-learn** / **XGBoost** — ML backend
- **Pydantic** — Validation
- **Uvicorn** — ASGI server

---

## 📌 TODOs

- [ ] Add authentication (e.g., API key)
- [ ] Logging and monitoring
- [ ] Dockerize the project
- [ ] Deploy on cloud (Heroku, AWS, etc.)

---

## 🧠 Credits

Made with ❤️ by [Your Name]  
For demo or educational purposes. Not suitable for financial production without testing and tuning.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
