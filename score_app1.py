# score_app.py 
import streamlit as st
st.title("성적표")
name= st.text_input("Enter your name")
# 과목 점수 입력
st.subheader("Enter your scores")
python = st.number_input("Python", min_value=0, max_value=100, step=1)
excel = st.number_input("Excel", min_value=0, max_value=100, step=1)
data = st.number_input("Digital Literacy", min_value=0, max_value=100, step=1)

# 계산 버튼
if st.button("Calculate"):
    total = python + excel + data
    avg = total / 3
    st.write(f"Name: **{name}**")
    st.write(f"Total Score: {total:.0f}") #st.success()로 써도 됨
    st.write(f"Average Score: {avg:.2f}")
    if avg >= 90:
        st.success("Grade: Excellent")
    elif avg >= 70:
        st.info("Grade: Good")
    else:
        st.warning("Grade: Try Again")
