import streamlit as st

st.title("Calculator")

placeholder = st.empty()

user_input = placeholder.text_input('Input Problem Here')
button_9 = st.button('9', key=3)
button_8 = st.button('8', key=2)
if button_9:
    user_input = placeholder.text_input('', value='9', key=1,)
