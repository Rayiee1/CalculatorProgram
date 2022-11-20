import streamlit as st

st.title("Calculator")

user_text = st.text_input("Input Your Problem")
if st.button("9"):
    st.write(9)