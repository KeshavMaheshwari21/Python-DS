import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import yfinance as yf
import datetime
from keras.models import load_model
import streamlit as st
from sklearn.preprocessing import MinMaxScaler

# Get current date and define start and end
current_datetime = datetime.datetime.now()
start = datetime.datetime(2014, 1, 1)
end = current_datetime.date()

# Title of the Streamlit app
st.title('Stock Trend Prediction')

# Input for stock ticker
user_input = st.text_input('Enter Stock Ticker', 'AAPL')

# Fetch stock data using yfinance
df = yf.download(user_input, start=start, end=end)

# Display data summary
st.subheader('Data from 2014 - 2024')
st.write(df.describe())

# Plot Closing Price vs Time
st.subheader('Closing Price vs Time Chart')
fig = plt.figure(figsize=(12,6))
plt.plot(df['Close'])
st.pyplot(fig)

# Plot Closing Price with 100MA and 200MA
st.subheader('Closing Price vs Time Chart with 100MA & 200MA')
ma100 = df['Close'].rolling(100).mean()
ma200 = df['Close'].rolling(200).mean()
fig = plt.figure(figsize=(12,6))
plt.plot(df['Close'], label='Closing Price', color='b')
plt.plot(ma100, label='100MA', color='r')
plt.plot(ma200, label='200MA', color='g')
plt.legend()
st.pyplot(fig)

# Splitting data into training and testing sets
data_train = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_test = pd.DataFrame(df['Close'][int(len(df)*0.70):])

# Scaling the data
scaler = MinMaxScaler(feature_range=(0,1))
data_train_array = scaler.fit_transform(data_train)

# Load pre-trained model
model = load_model('trend_model.h5')

# Prepare test data
past_100_days = data_train.tail(100)
final_df = pd.concat([past_100_days, data_test], ignore_index=True)
input_data = scaler.transform(final_df)  # Only transform using the fitted scaler, not fit again!

# Preparing x_test and y_test
x_test = []
y_test = []

for i in range(100, input_data.shape[0]):
    x_test.append(input_data[i-100:i])
    y_test.append(input_data[i, 0])

x_test, y_test = np.array(x_test), np.array(y_test)

# Predicting the stock prices
y_predicted = model.predict(x_test)

# Reversing the scaling to get the original scale of predicted values
scaler_factor = 1 / scaler.scale_[0]
y_predicted = y_predicted * scaler_factor
y_test = y_test * scaler_factor

# Plotting the predictions vs original prices
st.subheader('Predictions vs Original')
fig2 = plt.figure(figsize=(12,6))
plt.plot(y_test, label='Original Price', color='b')
plt.plot(y_predicted, label='Predicted Price', color='r')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig2)
