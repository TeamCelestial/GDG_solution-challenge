from fastapi import FastAPI
from pydantic import BaseModel
from backend.models import text_model, image_model, speech_model  # <-- Fix this import

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/predict/text")
async def predict_text(request: TextRequest):
    return {"prediction": text_model.predict(request.text)}

@app.post("/predict/image")
async def predict_image(image: str):
    # Assuming base64 encoded image
    image_data = decode_image(image)
    return {"predictions": image_model.detect_faces(image_data)}

@app.post("/predict/speech")
async def predict_speech(audio: str):
    return {"prediction": speech_model.detect_speech(audio)}

def decode_image(encoded_image):
    # Code to decode base64 to image
    return encoded_image  # Placeholder
