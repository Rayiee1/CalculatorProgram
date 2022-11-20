import streamlit as st

st.title("Calculator")

user_text = st.text_input('Input Your Problem', max_chars=None)
button_9 = st.button('9', key=3)
if button_9:
    user_text = st.text_input('', value='9', key=3,)
