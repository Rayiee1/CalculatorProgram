import streamlit as st

st.title('Calculator')

# creating a placeholder for the fixed sized textbox
logtxtbox = st.text_input()
logtxt = ''
logtxtbox.text_area("Enter Your Problem",logtxt)

Button_9 = st.button('9', key=1)
Button_8 = st.button('8', key=2)
if Button_9:
    logtxt += '9'
    logtxtbox.text_area("Enter Your Problem", logtxt,)
if Button_8:
    logtxt += '8'
    logtxtbox.text_area("Enter Your Problem", logtxt,)