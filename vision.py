from dotenv import load_dotenv
load_dotenv() #Importing all the environment variables
from PIL import Image

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Creating a function to load Gemini Pro model and get response
model = genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input, image):
    if input != " " :
        response = model.generate_content([input,image])
    else:     
        response = model.generate_content(image)
    return response.text


#Initializing streamlit app
st.set_page_config(page_title= "Gemini Image")
st.header("Gemini Vision Application")
input = st.text_input("Input: ", key = 'input')
# Restrict file types to JPEG and PNG
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open and display the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

submit = st.button("Describe image")

#On clicking submit
if submit:
    response = get_gemini_response(input, image)
    st.subheader("The response is")
    st.write(response)