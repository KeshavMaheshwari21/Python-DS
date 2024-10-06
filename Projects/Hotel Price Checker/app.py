import streamlit as st
import joblib
import numpy as np
from PIL import Image

model = joblib.load('./DecisionTreeRegressor.lb')

st.markdown(
    """
    <style>
    .stImage img {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)
image = Image.open('./back.jpg')
resized_image = image.resize((800, 300))

st.image(resized_image)

st.markdown(
    "<h1 style='text-align: center; color: white;'>Hotel Price Checker</h1>", 
    unsafe_allow_html=True
)

rating = st.number_input('Hotel Rating', min_value=1.0, max_value=5.0, step=0.2)
br = {'Ahmedabad': 0, 'Allahabad': 1, 'Amravati': 2, 'Amritsar': 3, 'Aurangabad': 4, 'Bangalore': 5, 'Bhubaneswar': 6, 'Chandigarh': 7, 'Chennai': 8, 'Coimbatore': 9, 'Dehradun': 10, 'Delhi': 11, 'Durgapur': 12, 'Faridabad': 13, 'Gandhinagar': 14, 'Ghaziabad': 15, 'Goa': 16, 'Guwahati': 17, 'Gwalior': 18, 'Hazaribagh': 19, 'Hyderabad': 20, 'Indore': 21, 'Jaipur': 22, 'Jamshedpur': 23, 'Kanpur': 24, 'Kanyakumari': 25, 'Kashmir': 26, 'Kochi': 27, 'Kolkata': 28, 'Kumarakom': 29, 'Lucknow': 30, 'Ludhiana': 31, 'Mangalore': 32, 'Meerut': 33, 'Mumbai': 34, 'Mysore': 35, 'Nagpur': 36, 'Nashik': 37, 'Noida': 38, 'Patna': 39, 'Pondicherry': 40, 'Pune': 41, 'Raipur': 42, 'Ranchi': 43, 'Sikkim': 44, 'Srinagar': 45, 'Trivandrum': 46, 'Vadodara': 47, 'Varanasi': 48, 'Varkala': 49, 'Vijayawada': 50}
city = st.selectbox('Select City', list(br.keys()))
city_encoded = br[city]

st.markdown(
    """
    <style>
    .stButton button {
        display: block;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button('Predict Price'):
    try:
        features = np.array([[rating, city_encoded]])
        
        predicted_price = model.predict(features)[0] 
        
        st.markdown(
            f"<h2 style='text-align: center; color: green; font-size: 30px;'>"
            f"Predicted Price : ₹{predicted_price:,.2f}</h2>",
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"An error occurred: {e}")
