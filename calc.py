import streamlit as st

st.title("Calculator")

placeholder = st.empty()

user_input = placeholder.number_input()
button_9 = st.button('9', key=9)
button_8 = st.button('8', key=8)
if button_9:
    user_input = placeholder.text_input('', value='9', key=9,)
