import yfinance as yf 
import streamlit as st
import pandas as pd

st.write("""
         # Simple Stock Price
         
         Shown are the stock closing price and volume of **Google**!
         
         """)
         
# Define ticker symbol
tickerSymbol = 'GOOGL'
# Get tick data
tickerData = yf.Ticker(tickerSymbol)
# Get historical data
tickerDf = tickerData.history(period='1d', start='2010-05-31', end='2023-12-31')

st.write("## Closing Price")
st.line_chart(tickerDf.Close)
st.write('## Volume Price')
st.line_chart(tickerDf.Volume)
