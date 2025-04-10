# 🏠 Predicted Interest Percentage API

This project trains a regression model to predict a user's **Predicted Interest Percentage** based on various demographic and housing-related features. It also provides a FastAPI-based REST API to serve predictions.

---

## 📁 Project Structure

```
.
├── data.csv                # Dataset with input features and target
├── train_model.py          # Script to train and save the ML model
├── api.py                  # FastAPI app for serving predictions
├── interest_model.pkl      # Trained model (generated after training)
└── README.md               # This file
```

---

## 🧠 Features Used for Prediction

- Budget
- LocationPreference
- JobType
- LoanEligibility
- TimeToBuy
- LeadSource
- ResidenceType
- PreferredBHK
- IsDecisionMaker
- PreviousInterest

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/dhirajdj30/Interest-Prediction-Model.git
cd vasu
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` yet, create one with:
```txt
fastapi
uvicorn
pandas
scikit-learn
joblib
```

### 3. Add Dataset
Place your `data.csv` file in the root directory. Format should match:

```
Budget,LocationPreference,JobType,...,PreviousInterest,PredictedInterestPercentage
```

---

## 🚀 Train the Model
```bash
python train_model.py
```
This will generate `interest_model.pkl`.

---

## 🌐 Start the API
```bash
uvicorn app:app --reload
```

- Access docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Access base endpoint: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧪 Example Prediction Request

### POST `/predict`

```json
{
  "Budget": 5000000,
  "LocationPreference": "Urban",
  "JobType": "Salaried",
  "LoanEligibility": "Eligible",
  "TimeToBuy": "0-3 Months",
  "LeadSource": "Referral",
  "ResidenceType": "Villa",
  "PreferredBHK": "3BHK",
  "IsDecisionMaker": "Yes",
  "PreviousInterest": "Yes"
}
```

### Response:
```json
{
  "PredictedInterestPercentage": 64.87
}
```

---


## 👨‍💻 Author

**Dhiraj Jagtap**  
*MLOps Engineer | AI/ML Developer*

---