import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Student Score")
st.divider()

np.random.seed(30)
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