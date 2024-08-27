# Import necessary libraries
from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

# Load environment variables from .env file
load_dotenv()

# Set up Google API key from environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a Gemini 1.5 Flash model instance
model = genai.GenerativeModel("gemini-1.5-flash")

# Define a function to get a response from the Gemini model
def get_gemini_response(input, image):
    # If input prompt is not empty, generate content with both input and image
    if input != "":
        response = model.generate_content([input, image])
    # If input prompt is empty, generate content with only the image
    else:
        response = model.generate_content(image)
    # Return the generated text response
    return response.text

# Set up Streamlit page configuration
st.set_page_config("Visualise your image")

# Add a header to the page
st.header("Visualise with Gemini")

# Create a text input field for the user to enter a prompt
input = st.text_input("Input Prompt: ", key="input")

# Create a file uploader for the user to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'png', 'jpeg'])

# Initialize an empty image variable
image = ''

# If an image is uploaded, open it using PIL and display it
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Create a submit button
submit = st.button("Tell me about the image")

# If the submit button is clicked, generate a response from the Gemini model
if submit:
    # Call the get_gemini_response function with the input prompt and image
    response = get_gemini_response(input, image)
    # Add a subheader to display the response
    st.subheader("The response is")
    # Display the generated response
    st.write(response)