import streamlit as st
from PIL import Image
import cv2
import numpy as np
import requests

st.title("Crowd Emotion Recognition")
st.write("""
This project implements a system for crowd emotion recognition, aiming to automatically classify the emotions present within a crowd image or video.
""")

st.sidebar.title("Options")
option = st.sidebar.selectbox("Choose an option", ["Upload Image", "Capture Image", "Upload Video", "Capture Video", "Display Name"])

# Function to upload image
def upload_image():
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

# Function to upload video
def upload_video():
    uploaded_file = st.file_uploader("Upload Video", type=["mp4"])
    if uploaded_file is not None:
        st.video(uploaded_file)

# Function to capture image from camera
def capture_image():
    st.write("Please look at the camera and press the 'Capture' button to take a picture.")
    if st.button("Capture"):
        capture = cv2.VideoCapture(0)
        ret, frame = capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            st.image(frame, caption="Captured Image", use_column_width=True)
            capture.release()
        else:
            st.error("Failed to capture image.")

# Function to capture video from camera
def capture_video():
    st.write("Please look at the camera and press the 'Start Recording' button to record a video.")
    if st.button("Start Recording"):
        capture = cv2.VideoCapture(0)
        out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20.0, (640, 480))
        recording = True
        while recording:
            ret, frame = capture.read()
            if ret:
                out.write(frame)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                st.image(frame, caption="Recording...", use_column_width=True)
                if st.button("Stop Recording"):
                    recording = False
            else:
                st.error("Failed to record video.")
                recording = False
        out.release()
        capture.release()

def display_name():
    name = st.text_input("Enter your name")
    if name:
        res = requests.post(url = "http://127.0.0.1:8000/name", data = {"name": name})
        text = res.json()["message"]
        text = f"Hello {text}"
        st.write(text)
        # st.write(res.text)

if option == "Upload Image":
    upload_image()
elif option == "Upload Video":
    upload_video()
elif option == "Capture Image":
    capture_image()
elif option == "Capture Video":
    capture_video()
elif option == "Display Name":
    display_name()
    


# Footer instructions
st.markdown("""
<footer style='text-align:center; position: fixed; bottom: 0; width: 50%;'>
    <p><b>The future of emotional intelligence | Crowd Emotion Recognizer | Developed by Zunaira and Darban |</b></p>
    <p><b>Supervised by Dr. Ali Raza!</b></p>
</footer>
""", unsafe_allow_html=True)


# streamlit run frontend/main.py