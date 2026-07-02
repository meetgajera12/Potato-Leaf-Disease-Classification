import streamlit as st
import requests
from PIL import Image

API_URL = "http://localhost:8000/predict"

st.set_page_config(page_title="Potato Disease Detection",
    page_icon="🥔",
    layout="centered")


st.title = ("🥔Patato Dieseases Ditection")

st.markdown("upload image below")

uploaded_file = st.file_uploader("Choose an image", type=['jpg','jpeg','png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption='Your Uploaded File')


if st.button('Predict'):
    files = {
        "file":(
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type
        )
    }

    with st.spinner('Predicting...'):
        responce = requests.post(API_URL, files=files)

    if responce.status_code == 200:
        result = responce.json()
        st.success("Prediction Complete!")
        st.subheader(f"Prediction: {result['class']}")
        st.subheader(f"Confidence: {result['confidence']*100:.2f}")
    else:
        st.error("Prediction Failed!")
        st.write(responce.text)