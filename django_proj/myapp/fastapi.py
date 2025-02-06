from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
from transformers import BertTokenizer
import os

# Import custom functions
from .tokenizer import (
    text_clean_for_bert, 
    clean_and_tokenize_single_text
)

# Initialize FastAPI app
app = FastAPI()

# Request model for unique prediction
class PredictionRequest(BaseModel):
    text: str
    model_type: int  # Specifies which model to use

# Load models on startup
@app.on_event("startup")
def load_model():
    print("Server startup - models are ready!")

# Unique Prediction Endpoint
@app.post("/predict/")
def predict(request: PredictionRequest):
    try:
        # Load the appropriate model
        #model_file = f"model{request.model_type}.pth"
        model_file = os.path.join(os.path.dirname(__file__), f"model{request.model_type}.pth")
        try:
            model = torch.load(model_file, map_location=torch.device('cpu'))
            model.eval()
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail=f"Model {model_file} not found")

        # Clean and tokenize the input text
        input_ids, attention_mask = clean_and_tokenize_single_text(request.text)
        input_ids, attention_mask = input_ids.unsqueeze(0), attention_mask.unsqueeze(0)

        # Perform inference
        with torch.no_grad():
            outputs = model(input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            prediction = torch.argmax(logits, dim=1).item()

        return {"prediction": prediction}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Health Check Endpoint
@app.get("/")
def read_root():
    return {"message": "Model API is ready!"}
