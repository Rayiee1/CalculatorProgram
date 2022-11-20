import streamlit as st

st.title('Calculator')

# creating a placeholder for the fixed sized textbox
logtxtbox = st.empty()
logtxt = ''
logtxtbox.text_area("Enter Your Problem",logtxt)

Button_9 = st.button('9', key=1)
if Button_9:
    logtxt += '9'
    logtxtbox.text_area("Enter Your Problem", logtxt,)