from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
from transformers import pipeline
import torch

app = FastAPI(
    title       = "Sentiment Analysis API",
    description = "DistilBERT fine-tuned on IMDB reviews",
    version     = "1.0.0"
)

# Load model once at startup
MODEL_PATH = "./saved_model"
pipe = pipeline(
    "text-classification",
    model   = MODEL_PATH,
    device  = 0 if torch.cuda.is_available() else -1
)

class TextRequest(BaseModel):
    texts: list[str]

    @validator('texts')
    def not_empty(cls, v):
        if not v:
            raise ValueError("texts list cannot be empty")
        if len(v) > 100:
            raise ValueError("max 100 texts per request")
        return v

class PredictionResult(BaseModel):
    text       : str
    label      : str
    confidence : float

@app.post("/predict", response_model=list[PredictionResult])
async def predict(req: TextRequest):
    try:
        results = pipe(req.texts, truncation=True, max_length=256)
        return [
            PredictionResult(
                text       = req.texts[i],
                label      = "POSITIVE" if r['label'] == 'LABEL_1' else "NEGATIVE",
                confidence = round(r['score'], 4)
            )
            for i, r in enumerate(results)
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok", "model": "distilbert-imdb"}

@app.get("/")
def root():
    return {"message": "Sentiment Analysis API", "docs": "/docs"}