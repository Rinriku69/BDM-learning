import streamlit as st

st.title('First page')

st.write(st.session_state)

st.write(st.session_state['num1'])
st.write(st.session_state['num2'])