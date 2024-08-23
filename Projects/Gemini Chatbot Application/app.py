from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st
from PIL import Image

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the generative AI model
genai.configure(api_key=API_KEY)

# Function to get a response from the Gemini model
def get_gemini_response(input_message, input_image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    if input_message != "":
        response = model.generate_content([input_message, input_image])
    else:
        response = model.generate_content(input_image)
    return response.text    

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Gemini LLM Application",
    page_icon=":crystal_ball:",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Add a stylish header with some formatting
st.markdown(
    """
    <h1 style='text-align: center;margin-top:-20px;'>
        Gemini LLM Application
    </h1>
    <p style='text-align: center; font-size: 22px;'>
        Enter a prompt or upload an image to interact with the Model!
    </p>
    """, unsafe_allow_html=True
)

# Input section with more user-friendly instructions
input = st.text_input("Input Prompt :", placeholder="Type your prompt here...", key="input")

# File uploader with a nicer layout
uploaded_file = st.file_uploader("Upload an Image (Optional):", type=['jpg', 'jpeg', 'png'], accept_multiple_files=False)

# Display the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.markdown(
        """
        <style>
        .center-image {
            width: 704px;
            margin-left: 35%;
            margin-top: 20px; /* Optional: to add some space above the image */
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.markdown('<div class="center-image">', unsafe_allow_html=True)
    st.image(image, caption="Uploaded Image", use_column_width=False)
    st.markdown('</div>', unsafe_allow_html=True)

# Center the button using custom CSS
st.markdown(
    """
    <style>
    div.stButton > button {
        display: block;
        margin: 0 auto;
    }
    </style>
    """, unsafe_allow_html=True
)

# Create the button
submit = st.button("Generate Response")

# Handle submission and display the response
if submit:
    if input or uploaded_file:
        with st.spinner("Generating response..."):
            response = get_gemini_response(input_message=input, input_image=image)
            st.subheader("Your Response:")
            st.markdown(
                f"""
                <div style='padding: 15px; border-radius: 10px;'>
                    {response}
                </div>
                """, unsafe_allow_html=True
            )
    else:
        st.warning("Please enter a prompt or upload an image.")
