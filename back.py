from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("linear_model.pkl")

class PropertyData(BaseModel):
    square_feet: float
    num_bedrooms: int
    num_bathrooms: int
    Num_Floors: int
    Year_Built: int
    Has_Garden: int  
    Has_Pool: int   
    Garage_Size: float
    Location_Score: int
    Distance_to_Center: float

@app.post("/predict")
def predict(data: PropertyData):
    features = np.array([[
        data.square_feet,
        data.num_bedrooms,
        data.num_bathrooms,
        data.Num_Floors,
        data.Year_Built,
        data.Has_Garden,    
        data.Has_Pool,      
        data.Garage_Size,
        data.Location_Score,
        data.Distance_to_Center
    ]])

    prediction = model.predict(features)[0]

    return {"price": float(prediction)}
