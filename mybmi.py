import streamlit as st
st.title("BMI")
#st.write("")
name=st.text_input("input your name")
h=st.number_input("Height")
w=st.number_input("Weight")

if h > 0:
    bmi = w / ((h/100) ** 2)
    st.write(f"{name}님의 BMI는 **{bmi:.2f}** 입니다.")
else:
    st.warning("키를 0보다 큰 값으로 입력해주세요.")

