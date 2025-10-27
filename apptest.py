import streamlit as st
st.title("TITEL")
st.write("Text")
st.text_input("input your name")
h=st.number_input("Height")
w=st.number_input("Weight")
st.write("BMI:",w/h**2)
