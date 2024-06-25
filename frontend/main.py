import streamlit as st
from PIL import Image
import cv2
import tempfile
import time
import numpy as np
from keras.preprocessing import image as keras_image # type: ignore
from support.emotion_detection import detect_emotion_in_image, detect_emotion_in_video, load_saved_model

st.set_page_config(page_title="Crowd Emotion Recognition")
st.title("Crowd Emotion Recognition")

st.markdown("""
    <p>This project implements a system for crowd emotion recognition, aiming to automatically classify the emotions present within a crowd image or video</p>
""", unsafe_allow_html=True)

model = load_saved_model()

def add_boundary():
    st.markdown(
        "<br><hr style='border: 1px solid white; border-radius: 2px;'>",
        unsafe_allow_html=True
    )

def clear_cache():
    st.session_state.clear()

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("##### Browse Image or Video from the System")
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png", "mp4", "avi", "mov"])

if uploaded_file is not None:
    clear_cache()
    file_type = uploaded_file.type.split('/')[0]
    if file_type == 'image':
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=False)
        image_path = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg").name
        image.save(image_path)
    elif file_type == 'video':
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        video_path = tfile.name
        st.video(video_path)

add_boundary()

# Section for capturing or recording image and video
st.markdown("##### Capture or Record Image and Video")
capture_col1, capture_col2 = st.columns(2)

captured_image = None
captured_video_path = None

with capture_col1:
    if st.button("Capture Image"):
        time.sleep(1)  # 1-second pause before starting the capture
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if ret:
            captured_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            st.session_state['captured_image'] = captured_image
            st.write("Image captured successfully")
        else:
            st.error("Failed to capture image")

    if st.button("Record Video"):
        time.sleep(1)  # 1-second pause before starting the recording
        st.write("Recording for 5 seconds...")
        cap = cv2.VideoCapture(0)
        codec = cv2.VideoWriter_fourcc(*"mp4v")  # Save as MP4 format
        video_filename = "captured_video.mp4"
        out = cv2.VideoWriter(video_filename, codec, 20.0, (640, 480))
        for _ in range(100): 
            ret, frame = cap.read()
            if ret:
                out.write(frame)
            else:
                break
        cap.release()
        out.release()
        captured_video_path = video_filename
        st.session_state['captured_video_path'] = captured_video_path
        st.write("Video recorded successfully")

with capture_col2:
    if 'captured_image' in st.session_state:
        st.image(st.session_state['captured_image'], caption='Captured Image', use_column_width=True)
    if 'captured_video_path' in st.session_state:
        st.video(st.session_state['captured_video_path'])

add_boundary()
st.markdown("##### Display Result")
result_col1, result_col2 = st.columns(2)

with result_col1:
    if st.button("Get Result"):
        if uploaded_file is not None:
            if file_type == 'image':
                emotion = detect_emotion_in_image(model, image_path)
                st.session_state['result'] = emotion
            elif file_type == 'video':
                emotion = detect_emotion_in_video(model, video_path)
                st.session_state['result'] = emotion
        elif 'captured_image' in st.session_state:
            captured_image_path = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg").name
            st.session_state['captured_image'].save(captured_image_path)
            emotion = detect_emotion_in_image(model, captured_image_path)
            st.session_state['result'] = emotion
        elif 'captured_video_path' in st.session_state:
            emotion = detect_emotion_in_video(model, st.session_state['captured_video_path'])
            st.session_state['result'] = emotion

with result_col2:
    if 'result' in st.session_state:
        st.write(f"Detected Emotion: {st.session_state['result']}")
    else:
        st.write("No emotion detected yet.")

st.markdown("""
    <style>
    .footer {
        position: relative;
        bottom: 0;
        width: 100%;
        text-align: center;
    }
    </style>
    <div class="footer">
        <p><b>The future of emotional intelligence | Crowd Emotion Recognizer | Developed by Zunaira and Darban |</b></p>
        <p><b>Supervised by Dr. Ali Raza!</b></p>
    </div>
""", unsafe_allow_html=True)

