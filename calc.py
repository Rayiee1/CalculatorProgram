import streamlit as st
import time

st.title('Calculator')

# creating a placeholder for the fixed sized textbox
logtxtbox = st.empty()
logtxt = 'start'
logtxtbox.text_area("Enter Problem",logtxt)

end_of_loop = False
counter = 1

while (end_of_loop==False):

    logtxt += 'Counter [' + str(counter) + '] \n'
    logtxtbox.text_area("Proble Here", logtxt,)

    counter += 1
    if (counter > 100):
        end_of_loop = True

    time.sleep(0.2)