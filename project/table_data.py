import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Student Score")
st.divider()

np.random.seed(30)
student_score = pd.read_csv('WebPro.csv')
df= student_score.drop('NO',axis=1)
df = df.set_index('Student ID')
df = df.apply(pd.to_numeric,errors='coerce')
df_clean = df.dropna()
df_clean['Total'] =df_clean.sum(axis=1)
score = np.random.randint(1,101,size=(3,4))
students = ['Student1','Student2','Student3']
subjects = ['Math','English','Programming','Thai']

df = pd.DataFrame(score,students,subjects)
df.index.name = "Student"

st.caption((',').join([i for i in subjects]))
st.write(df.head(3))
#st.table(df)

st.metric(label="Metric label", value=900, delta=20, delta_color="inverse") #normal for positive changes

st.bar_chart(df,x_label="Student",y_label="Score",stack=False,)

fig, ax = plt.subplots()

df.plot(kind='bar', ax=ax)

ax.set_title("All subject scores")
ax.set_ylabel("Score")

st.pyplot(fig)



st.divider()

#button
primary_btn = st.button(label="Button 1", type="primary",help="click me",)
secondary_btn= st.button(label="Button 2", type='secondary')

if(primary_btn):
    st.write("Primary Butoon clicked")
if(secondary_btn):
    st.write("Secondary Butoon clicked")

#checkbox
checkbox= {}
for i in range(len(df_clean.keys())): 
    checkbox[i] = st.checkbox(df_clean.keys()[i])

checked = [j for j in checkbox.keys() if checkbox[j] == True]
checked_column = []

if(len(checked) >= 1):
 checked_column.extend(df_clean.columns[checked])
 st.write(df_clean[checked_column])

st.divider()
#radio
radio= st.radio("Choose a column", options=df_clean.columns[0:],index=1,horizontal=False)

st.write(df_clean[radio])

st.divider()

#select box
select = st.selectbox("Choose a column", options=df_clean.columns[0:])

st.write(df_clean[select])
st.divider()
#Multi select
mul_select = st.multiselect("Choose columns",options=df_clean.columns[0:],default='affective',max_selections=4)
st.write(df_clean[mul_select])
st.divider()

#slider
slider = st.slider("slider",min_value=0,max_value=100,value=30,step=1)
st.write(df_clean[df_clean['Total']>slider])
st.divider()

#text input
text = st.text_input("Input text",placeholder="ex. John Doe")

st.write(text)
st.divider()

#number input
num_input = st.number_input("Inuput number",min_value=0,max_value=100,value=0,step=1)
st.write(df_clean[df_clean['Total']>num_input])
st.divider()

#text area
text_area = st.text_area("Write text",height=200)
st.write(text_area)


