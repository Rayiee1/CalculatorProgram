import streamlit as st

st.title("Calculator")

user_text = st.text_input("Input Your Problem", Value = "here", max_chars = None,)
if st.button("9"):
    st.text_input(9)