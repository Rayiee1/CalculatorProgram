import streamlit as st

st.title("Calculator")

user_text = st.text_input("Input Your Problem", max_chars=None)
if st.button("9"):
    upadate_text = st.text_input("9")
