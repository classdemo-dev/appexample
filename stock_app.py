# 파일명: stock_app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

st.title("📈 주가 시각화 대시보드")

symbol = st.text_input("티커(symbol) 입력 (예: AAPL, TSLA, NVDA, 005930.KS)", "AAPL")
period = st.selectbox("기간 선택", ["1mo", "3mo", "6mo", "1y", "2y", "5y"], index=3)
interval = st.selectbox("간격", ["1d", "1wk", "1mo"], index=0)

if st.button("데이터 불러오기"):
    with st.spinner("데이터 가져오는 중..."):
        data = yf.download(symbol, period=period, interval=interval)
    if data.empty:
        st.error("데이터가 없습니다. 심볼/기간을 확인하세요.")
    else:
        st.success(f"{symbol} 데이터 로드 완료!")
        st.dataframe(data.tail())

        fig, ax = plt.subplots()
        ax.plot(data.index, data["Close"])
        ax.set_title(f"{symbol} 종가({period}, {interval})")
        ax.set_xlabel("날짜"); ax.set_ylabel("가격")
        st.pyplot(fig)

        st.download_button(
            "CSV 다운로드",
            data.to_csv().encode("utf-8"),
            file_name=f"{symbol}_{period}_{interval}.csv",
            mime="text/csv"
        )
