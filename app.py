from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the model
model = joblib.load("interest_model.pkl")

app = FastAPI()

# Input schema
class InterestInput(BaseModel):
    Budget: int
    LocationPreference: str
    JobType: str
    LoanEligibility: str
    TimeToBuy: str
    LeadSource: str
    ResidenceType: str
    PreferredBHK: str
    IsDecisionMaker: str
    PreviousInterest: str

@app.get("/")
def read_root():
    return {"message": "🎯 Welcome to the Predicted Interest API!"}

@app.post("/predict")
def predict(input_data: InterestInput):
    # Convert input to DataFrame
    input_df = pd.DataFrame([input_data.dict()])
    # Make prediction
    prediction = model.predict(input_df)[0]
    return {"PredictedInterestPercentage": round(prediction, 2)}
