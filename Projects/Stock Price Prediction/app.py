import streamlit as st
import yfinance as yf
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import joblib
from datetime import datetime

# Load your trained model and scaler
model = load_model('model.h5')  # Update with your model path
scaler = joblib.load('scaler.lb')  # Update with your scaler path

# Example list of available tickers (you can expand this list)
available_tickers = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NFLX', 'NVDA',
    'IBM', 'ORCL', 'INTC', 'CSCO', 'DIS', 'BA', 'WMT', 'MA', 'V', 'HD', 'PG'
]

def get_prediction(ticker, date):
    # Download historical data
    try:
        stock_data = yf.download(ticker, start='2012-01-01', end='2024-09-11')
        if stock_data.empty:
            return None, "Data for the ticker symbol is not available."
        
        new_df = stock_data[['Close']]

        # Prepare the data
        last_60_days = new_df[-60:].values
        last_60_days_scaled = scaler.transform(last_60_days)
        X_test = np.array([last_60_days_scaled])
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

        # Fetch latest price for the given date
        latest_price_data = yf.download(ticker, start=date, end=date)
        latest_price = latest_price_data['Close'].values[0] if not latest_price_data.empty else None

        # Predict the price
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)

        return latest_price, float(pred_price[0])
    except Exception as e:
        return None, str(e)

# Streamlit app
st.title('Stock Price Prediction')

# Input for stock ticker
ticker = st.selectbox("Select Stock Ticker:", available_tickers)

# Input for date
date_input = st.date_input("Select Date:")
date_str = date_input.strftime('%Y-%m-%d')

if st.button('Get Prediction'):
    latest_price, result = get_prediction(ticker, date_str)
    
    if latest_price is not None:
        st.write(f"Latest Price for {ticker} on {date_str}: ${latest_price:.2f}" if latest_price is not None else "Latest price data is not available.")
        st.write(f"Predicted Price for {ticker}: ${result:.2f}")
    else:
        st.error(result)
