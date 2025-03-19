import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google!
""")

# Define the ticker symbol
tickerSymbol = 'GOOGL'
# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# Get the historical prices for this ticker using start and end dates only
tickerDf = tickerData.history(start='2010-05-31', end='2020-05-31')
# Open, High, Low, Close, Volume, Dividends, Stock Splits

st.line_chart(tickerDf['Close'])
st.line_chart(tickerDf['Volume'])
