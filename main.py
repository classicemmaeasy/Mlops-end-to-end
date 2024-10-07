from fastapi import FastAPI
import pickle
import pandas as pd
from data_model import Water


app=FastAPI(
    title="water portability",
    description="predicting water Portability")


with open(r"C:\Users\HP\Documents\MLOPS\model.pkl","rb") as f:
    model=pickle.load(f)

@app.get("/")

def index():
    return "welcome to water portability prediction FastAPI"


@app.post("/predict")
def model_predict(water:Water):
    sample=pd.DataFrame({
        'ph':[water.ph],
        'Hardness':[water.Hardness],
        'Solids':[water.Solids],
        'Chloramines':[water.Chloramines],
        'Sulfate':[water.Sulfate],
        'Conductivity':[water.Conductivity],
        'Organic_carbon':[water.Organic_carbon],
        'Trihalomethanes':[water. Trihalomethanes],
        'Turbidity':[water.Turbidity],
    })


    predicted_val=model.predict(sample)

    if predicted_val == 1:
      return "Water is consumable"
    else:
      return "Water is not consumable" 
    
