# 파일명: stock_app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

st.title("주가 시각화 대시보드")
symbol = st.text_input("종목 입력 (예: AAPL, TSLA, NVDA, 005930.KS)", "AAPL")
period = st.selectbox("기간 선택", ["1mo", "3mo", "6mo", "1y", "2y", "5y"], index=3)
interval = st.selectbox("간격", ["1d", "1wk", "1mo"], index=0)
st.caption("데이터 출처: Yahoo Finance (https://finance.yahoo.com/)")
data = yf.download(symbol, period=period, interval=interval)
price = st.write(data["Close"].iloc[-1])

plt.plot(data.index, data["Close"])
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.title(f"{symbol} 종가({period}, {interval})")
plt.xlabel("기간")
plt.ylabel("가격")
st.pyplot(plt)
