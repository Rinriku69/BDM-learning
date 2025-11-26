import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def grading(total):
    if total >= 80:
        return "A"
    elif total >= 75:
        return "B+"
    elif total >= 70:
        return "B"
    elif total >= 65:
        return "C+"
    elif total >= 60:
        return "C"
    elif total >= 55:
        return "D+"
    elif total >= 50:
        return "D"
    else :
        return "F"
    
            

student_score = pd.read_csv('WebPro.csv')
df = pd.DataFrame(student_score)
df = df.set_index('Student ID')
df_dropNO = df.drop('NO',axis=1)
df_clean = df_dropNO.apply(pd.to_numeric, errors='coerce')
df_clean = df_clean.dropna()
df_clean['Total'] = df_clean.sum(axis=1)
df_clean['grade'] = df_clean['Total'].apply(grading)



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
st.divider()

score_info = df_clean.describe()
st.dataframe(score_info)
st.divider()

st.dataframe(df_clean)
