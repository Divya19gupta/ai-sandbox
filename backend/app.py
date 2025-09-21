from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware

# Load sentiment model using PyTorch
model = pipeline("sentiment-analysis", framework="pt")

# Initialize FastAPI
app = FastAPI()

# Enable CORS for frontend (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in production, replace "*" with frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input schema
class TextInput(BaseModel):
    text: str

# POST endpoint
@app.post("/analyze")
def analyze_sentiment(input: TextInput):
    res = model(input.text)
    return {"label": res[0]["label"], "score": res[0]["score"]}
