import streamlit as st
from datetime import datetime, timedelta


st.header('Session state')

st.slider('Slider',0,100,key='slider',value=50)

st.write(st.session_state)

if 'num_input' not in st.session_state:
    st.session_state['num_input'] = 5

st.number_input('Input Number',0,100,key='num_input')

st.subheader('Callback')

st.markdown('#### Select time range')

def add_timedelta():
    initial = st.session_state['start_date']
    if st.session_state['time_range'] == '7 days':
        st.session_state['end_date'] = initial + timedelta(days=7)
    elif st.session_state['time_range'] == '28 days':
        st.session_state['end_date'] = initial + timedelta(days=28)
    else:
        pass
def minus_timedelta():
    end_date = st.session_state['end_date']
    if st.session_state['time_range'] == '7 days':
        st.session_state['start_date'] = end_date - timedelta(days=7)
    elif st.session_state['time_range'] == '28 days':
        st.session_state['start_date'] = end_date - timedelta(days=28)
    else:
        pass
    

    
st.radio('',options=['7 days','28 days','custom'],horizontal=True,key='time_range',on_change=add_timedelta)

col1, col2 = st.columns(2)
col1.date_input('Start',key='start_date', on_change=add_timedelta)
col2.date_input('End',key='end_date', on_change=minus_timedelta)
