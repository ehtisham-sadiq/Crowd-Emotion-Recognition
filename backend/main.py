from fastapi import FastAPI, Form, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import cv2
from PIL import Image
from io import BytesIO
import numpy as np

app = FastAPI()

# Allow all origins to enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/name")
async def name(name: str= Form(...)):
    return {"message": f"{name}"}

@app.post("/image_emotion")
async def detect_emotion_from_image(image: UploadFile = File(...)):
    contents = await image.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # Now, you can perform emotion detection on the image
    return {"message": f"Emotion detection from image will be performed here{img}"}

@app.post("/video_emotion")
async def detect_emotion_from_video(video: UploadFile = File(...)):
    contents = await video.read()
    # You can save the video file and perform emotion detection on it
    return {"message": f"Emotion detection from video will be performed here{contents}"}

@app.get("/complete_model_results")
async def complete_model_results():
    return {"message": "Complete model results will be shown here"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


# uvicorn backend.main:app --reload
