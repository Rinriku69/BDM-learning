import streamlit as st
import time


st.title("Caching")

st.button("Test")

@st.cache_data
def cacahe_test():
    time.sleep(5)
    out = "Output"
    
    return out


out = cacahe_test()
st.write(out)



