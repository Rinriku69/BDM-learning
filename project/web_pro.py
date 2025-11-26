import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

student_score = pd.read_csv('WebPro.csv')
df = pd.DataFrame(student_score)
df = df.set_index('Student ID')
df_dropNO = df.drop('NO',axis=1)
df_clean = df_dropNO.apply(pd.to_numeric, errors='coerce')
df_clean = df_clean.dropna()
df_clean['Total'] = df_clean.sum(axis=1)


fig, ax = plt.subplots()

df_clean.plot(kind='scatter',x='midterm',y='final',ax=ax, alpha=0.5)
ax.set_title('Midterm and Final')

st.markdown("## matplot scatter")
st.pyplot(fig)
st.divider()
st.markdown("## Streamlit Scatter")
st.scatter_chart(df_clean,x='midterm',y='final')
st.divider()

df_sort = df_clean.sort_values('Total')

st.bar_chart(df_sort.tail(10),y='Total')

