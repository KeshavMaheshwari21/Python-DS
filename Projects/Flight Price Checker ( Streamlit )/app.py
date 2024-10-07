import streamlit as st
import joblib
import numpy as np
from PIL import Image

model = joblib.load('Flight_Model.lb')

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
resized_image = image.resize((800, 400))

st.image(resized_image)

st.markdown(
    "<h1 style='text-align: center; color: white;'>Flight Price Predictor</h1>", 
    unsafe_allow_html=True
)

# Input for Flight Duration
duration = st.number_input('Enter the Duration of Flight (in hours):', min_value=1, max_value=24, step=1)

# Input for Days Left
days_left = st.number_input('Enter the number of Days Left:', min_value=1, max_value=365, step=1)

# Airline Selection
airline_options = ['AirAsia', 'Air India', 'Go First', 'Indigo', 'SpiceJet', 'Vistara']
airline = st.selectbox('Select Airline:', airline_options)

# Mapping airline input
airline_values = [1 if airline == a else 0 for a in airline_options]

# Source City Selection
source_city_options = ['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai']
source_city = st.selectbox('Select Source City:', source_city_options)

# Mapping source city input
source_city_values = [1 if source_city == s else 0 for s in source_city_options]

# Departure Time Selection
departure_time_options = ['Afternoon', 'Early Morning', 'Evening', 'Late Night', 'Morning', 'Night']
departure_time = st.selectbox('Select Departure Time:', departure_time_options)

# Mapping departure time input
departure_time_values = [1 if departure_time == d else 0 for d in departure_time_options]

# Arrival Time Selection
arrival_time = st.selectbox('Select Arrival Time:', departure_time_options)

# Mapping arrival time input
arrival_time_values = [1 if arrival_time == a else 0 for a in departure_time_options]

# Destination City Selection
destination_city = st.selectbox('Select Destination City:', source_city_options)

# Mapping destination city input
destination_city_values = [1 if destination_city == d else 0 for d in source_city_options]

# Number of Stops Selection
stops_options = ['Zero Stops', 'One Stop', 'Two or More Stops']
stops = st.selectbox('Select Number of Stops:', stops_options)

# Mapping number of stops input
stops_values = [1 if stops == s else 0 for s in stops_options]

# Flight Class Selection
flight_class_options = ['Economy', 'Business']
flight_class = st.selectbox('Select Class:', flight_class_options)

# Mapping flight class input
class_values = [1 if flight_class == flight_class_options[1] else 0,  # Business class
                1 if flight_class == flight_class_options[0] else 0]  # Economy class

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
        # Combine all input features into a single list
        input_features = [duration, days_left] + airline_values + source_city_values + departure_time_values + \
                         stops_values + arrival_time_values + destination_city_values + class_values

        # Convert to numpy array and reshape for prediction
        features = np.array(input_features).reshape(1, -1)

        # Predicting the price using the model
        predicted_price = model.predict(features)[0]

        st.markdown(
            f"<h2 style='text-align: center; color: green; font-size: 30px;'>"
            f"Predicted Price : ₹{predicted_price:,.2f}</h2>",
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"An error occurred: {e}")
