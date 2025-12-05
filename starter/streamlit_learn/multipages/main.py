import streamlit as st
import pandas as pd

# page config
st.set_page_config(
    page_title="Halo",
    page_icon="😘",
    layout="centered",
    initial_sidebar_state="expanded",
)

if all(key not in st.session_state.keys() for key in('num1','num2')):
    st.session_state['num1']=0
    st.session_state['num2']=0

df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})

if "df" not in st.session_state:
    st.session_state["df"] = df


def keep(key):
    st.session_state[key] = st.session_state[f"_{key}"]


def unkeep(key):
    st.session_state[f"_{key}"] = st.session_state[key] 

if __name__ == "__main__":
    st.title("Home")
    unkeep('num1')
    st.number_input('num1',key='_num1',on_change=keep,args=(("num1",)))
    unkeep('num2')
    st.number_input('num2',key='_num2',on_change=keep,args=(("num2",)))

    
    
    st.write(st.session_state)
