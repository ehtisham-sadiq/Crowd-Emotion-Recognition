from deepface import DeepFace
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
from pathlib import Path
import uvicorn

app = FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/analyze-emotion/")
async def analyze_emotion(file: UploadFile = File(...)):
    file_location = UPLOAD_DIR / file.filename
    with file_location.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    analysis = DeepFace.analyze(img_path=str(file_location), actions=["emotion"])

    emotion_scores = analysis[0]["emotion"]
    dominant_emotion = analysis[0]["dominant_emotion"]
    return JSONResponse(content={"dominant_emotion": dominant_emotion, "emotion_scores": emotion_scores})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
