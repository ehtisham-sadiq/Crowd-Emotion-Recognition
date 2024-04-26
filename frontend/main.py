# Here all the streamlit and frontend code is avaiable
import streamlit as st
from PIL import Image

st.title("Crowd Emotion Recognition")
st.write("""
This project implements a system for crowd emotion recognition, aiming to automatically classify the emotions present within a crowd image or video.
""")

st.sidebar.title("Options")
option = st.sidebar.selectbox("Choose an option", ["Upload Image", "Upload Video"])

# Function to upload image
def upload_image():
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        # Perform emotion prediction on the uploaded image
        # Show the predicted emotion(s) below the image

# Function to upload video
def upload_video():
    uploaded_file = st.file_uploader("Upload Video", type=["mp4"])
    if uploaded_file is not None:
        st.video(uploaded_file)
        # Perform emotion prediction on the uploaded video
        # Show the predicted emotion(s) below the video

if option == "Upload Image":
    upload_image()
elif option == "Upload Video":
    upload_video()
