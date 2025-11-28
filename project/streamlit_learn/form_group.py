import streamlit as st
import pandas as pd


student_score = pd.read_csv('WebPro.csv')
df= student_score.drop('NO',axis=1)
df = df.set_index('Student ID')
df = df.apply(pd.to_numeric,errors='coerce')
df_clean = df.dropna()
df_clean['Total'] =df_clean.sum(axis=1)
menus = ['Pepsi','Coke']

with st.form("key_form"):

    select_box = st.selectbox("Select your menu", options=menus)
    date = st.date_input("date")
    time_inputs = st.time_input("Time",value='00:00')
    text = st.text_input("input")
    check_box = st.checkbox("R u gay?")
    submit_btn = st.form_submit_button("Submit",type='primary')

st.write(f"""{date}
         {"yes" if check_box else "no"}
         """)

#side bar
with st.sidebar:
    st.write("text")

#columns
col1, col2, col3 = st.columns(3)
col1.write("text col1")

slider = col2.slider("choose number",min_value=0,max_value=100)

new_btn = col3.button("col3 button",type='primary')

#tab

tab1, tab2 = st.tabs(['Line','Bar'])

tab1.line_chart(df_clean,x='final',y='midterm')
tab2.bar_chart(df_clean.head(10),x_label="Student ID",y_label="Score",stack=False)
st.divider()
#expander
with st.expander("Click to see more information"):
    tab1, tab2 = st.tabs(['Line','Bar'])

    tab1.line_chart(df_clean,x='final',y='midterm')
    tab2.bar_chart(df_clean.head(10),x_label="Student ID",y_label="Score",stack=False)
    st.divider()
    st.write(df_clean.describe())

#container
with st.container(border=True):
    st.write("inside Container")

st.write("outside Container")