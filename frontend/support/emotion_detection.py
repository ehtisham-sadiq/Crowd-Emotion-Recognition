import cv2
import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image as keras_image # type: ignore
from keras.models import load_model  # type: ignore
from keras.preprocessing import image # type: ignore
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore

model_path = "model/resnet50_tt_fermod_68.h5"

def load_saved_model():
    resnet50_model = load_model(model_path)
    return resnet50_model

def emotion_analysis(emotions):
    objects = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
    y_pos = np.arange(len(objects))
    
    sns.set(style="whitegrid")
    sns.barplot(x=objects, y=emotions, palette="viridis")
    plt.ylabel('Percentage')
    plt.title('Emotion Analysis')
    plt.show()

def detect_emotion_in_image(model, image_path):
    d = {0:"angry",1:"disgust",2:"fear",3:"happiness",4:"sad",5:"surprise",6:"neutral"}
    face_cascade = cv2.CascadeClassifier('opencv/haarcascade_frontalface_alt.xml')
    t_image = cv2.imread(image_path)
    gray = cv2.cvtColor(t_image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if len(faces) == 0:
        return "No faces detected"
    for (x, y, w, h) in faces:
        cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 0, 0), 2)
        start_row, end_row, start_col, end_col = y, y+h, x, x+w
    cropped_image = gray[start_row:end_row, start_col:end_col]
    img = cv2.resize(cropped_image, (48, 48))
    x = keras_image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x /= 255
    custom = model.predict(x)
    emotion_analysis(custom[0])
    print(custom[0])
    emt = list(custom[0])
    idx = emt.index(max(emt))
    emotion = d[idx]
    print(f"Emotion in the image is : {emotion}")
    return emotion



def getFrame(seconds, vidcap, model, face_cascade, d, dcount):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,seconds*1000)
    hasFrames,img = vidcap.read()
    
    if hasFrames:
        minutes = "00"
        hours = "00"
        if seconds >= 60:
            minutes = str(seconds//60)
            seconds = seconds % 60

        if int(minutes) >= 60:
            hours = str(int(minutes)//60)
            minutes = str(int(minutes) % 60)

        min = "{:02d}".format(int(minutes))
        sec = "{:02d}".format(seconds)
        hrs = "{:02d}".format(int(hours))

        flag = 0 
        frameId = vidcap.get(1)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.1,4)
        
        if(len(faces)==0):
            flag = 1
        
        if flag == 0 :
            global count
            count = count + 1
            for (x,y,w,h) in faces:
                cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
                start_row,end_row,start_col,end_col = y,y+h,x,x+h  
            
            croppedimage = gray[start_row:end_row,start_col:end_col]
            finalimg = cv2.resize(croppedimage,(48,48))

            x = image.img_to_array(finalimg)
            x = np.expand_dims(x, axis = 0)

            x /= 255

            custom = model.predict(x)
            emt = list(custom[0])
            idx = emt.index(max(emt))
            imgname = d[idx]
            dcount[imgname] = dcount[imgname] + 1
            
            cv2.imwrite("/data/" + "%d_" % count +imgname+"__"+ hrs+":"+min+":"+sec+".jpg" ,img) 
    
    return hasFrames


def detect_emotion_in_video(model, video_path):
    # videoFile = "/Users/ehtishamsadiq/Crowd-Emotion-Recognition/backend/data/emotion_recognition_test_video.mp4"
    vidcap = cv2.VideoCapture(video_path)
    d = {
        0:"angry",
        1:"disgust",
        2:"fear",
        3:"happiness",
        4:"sad",
        5:"surprise",
        6:"neutral"
        }
    dcount = {
        "angry":0,
        "disgust":0,
        "fear":0,
        "happiness":0,
        "sad":0,
        "surprise":0,
        "neutral":0
        }

    face_cascade = cv2.CascadeClassifier('opencv/haarcascade_frontalface_alt.xml')
    count = 0
    sec = 0
    frameRate = 3 #it will capture image in each 2 second
    success = getFrame(sec, vidcap, model, face_cascade, d, dcount)
    while success:
        sec = sec + frameRate
        #sec = round(sec, 2)
        success = getFrame(sec, vidcap, model, face_cascade, d, dcount)

    print ("Done!")
    print("Extracted images:",count)
    print(dcount)
    emotions = list(dcount.keys())
    values = list(dcount.values())
    for key, value in dcount.items():
        if value == max(values):
            emotion = key
    emotion_analysis(values)
    return emotion

# def emotion_analysis(emotions):
#     objects = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
#     y_pos = np.arange(len(objects))
    
#     sns.set(style="whitegrid")
#     fig, ax = plt.subplots()
#     sns.barplot(x=objects, y=emotions, palette="viridis", ax=ax)
#     ax.set_ylabel('Percentage')
#     ax.set_title('Emotion Analysis')
    
#     st.pyplot(fig)

# Function to process image and detect emotion 
# def detect_emotion_in_image(model, image):
#     d = {0:"angry",1:"disgust",2:"fear",3:"happiness",4:"sad",5:"surprise",6:"neutral"}
#     face_cascade = cv2.CascadeClassifier('../opencv/haarcascade_frontalface_alt.xml')
#     # true_image = image.load_img(image) # actual image
#     t_image = cv2.imread(image)
#     gray = cv2.cvtColor(t_image,cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray,1.1,4)
#     if(len(faces) == 0):
#         exit()
#     for (x,y,w,h) in faces:
#         cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
#         start_row,end_row,start_col,end_col = y,y+h,x,x+h
#     croppedimage = gray[start_row:end_row,start_col:end_col]
#     img = cv2.resize(croppedimage,(48,48))
#     x = image.img_to_array(img)
#     x = np.expand_dims(x, axis = 0)
#     x /= 255
#     custom = model.predict(x)
#     emotion_analysis(custom[0])
#     print(custom[0])
#     emt = list(custom[0])
#     idx = emt.index(max(emt))
#     emotion = d[idx]
#     print(f"Emotion in the image is : {emotion}")
#     return emotion
