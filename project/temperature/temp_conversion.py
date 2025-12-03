import streamlit as st
def temp_change(temp_type):
    if temp_type == 'celsius':
        celsius = st.session_state['celsius']
        st.session_state['farenheit'] = (celsius * 9/5) + 32
        st.session_state['kelvin'] = celsius + 273.15
    elif temp_type == 'farenheit':
        farenheit = st.session_state['farenheit']
        st.session_state['celsius'] = (farenheit - 32)* 5/9
        st.session_state['kelvin'] = ((farenheit - 32)* 5/9) + 273.15
    elif temp_type == 'kelvin':
        kelvin = st.session_state['kelvin']
        st.session_state['celsius'] = kelvin - 273.15
        st.session_state['farenheit'] = ((kelvin - 273.15)*9/5)+32
    else:
        pass

def add_celsius(add_celsius_value):
    st.session_state['celsius'] = st.session_state['celsius'] + add_celsius_value
    temp_change('celsius')
    
def matter_state_change():
    state = st.session_state['matter_state']
    if state == '🧊Freezing point':
        st.session_state['celsius'] = 0
        temp_change('celsius')
    elif state == '🔥Boiling point':
        st.session_state['celsius'] = 100
        temp_change('celsius')
    elif state == '🥶Absolute zero':
        st.session_state['kelvin'] = 0
        temp_change('kelvin')   
    else:
        pass



st.header("Temperature Conversion")

st.subheader("Input form")

col1, col2, col3 = st.columns(3)

celsius = col1.number_input("Celsius",step=0.5,key="celsius",on_change=temp_change,kwargs={'temp_type' :'celsius'},value=0.00)
farenheit = col2.number_input("Farenheit",step=0.5,key="farenheit",on_change=temp_change,value=(celsius * 9/5) + 32,kwargs={'temp_type' :'farenheit'})
kelvin = col3.number_input("Kelvin",step=0.5,key="kelvin",on_change=temp_change,value =celsius + 273.15,kwargs={'temp_type' :'kelvin'})

add_celsius_value = col1.number_input("Add to celsius", step=0.5)
add_button = col1.button("Add",type='primary',on_click=add_celsius,kwargs={'add_celsius_value':add_celsius_value})

matter_state = st.radio('',options=['🧊Freezing point','🔥Boiling point','🥶Absolute zero'],horizontal=True,key='matter_state',
                        on_change=matter_state_change)

st.write(st.session_state)