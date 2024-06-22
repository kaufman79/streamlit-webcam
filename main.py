import cv2
from datetime import datetime
import streamlit as st


st.title("Webcam")
start = st.button("Start Camera")

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        now = datetime.now()
        weekday = now.strftime("%A")
        clock = now.strftime("%H:%M:%S")
        check, frame = camera.read()

        cv2.putText(img=frame, text=weekday, org=(20, 30),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1.5, color=(255, 255, 255),
                    thickness=1, lineType=cv2.LINE_AA)

        cv2.putText(img=frame, text=clock, org=(20, 55),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1.5, color=(255, 20, 20),
                    thickness=1, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)

