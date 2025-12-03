import streamlit as st


st.header('Session State')



st.button('Update State')

key_inputs = st.text_input("Input text",placeholder="ex. John Doe")

st.session_state['key']="hi"

st.write(st.session_state['key'])