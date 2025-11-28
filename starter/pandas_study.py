import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''student_scores = pd.read_csv('student_score.csv')
pd.DataFrame(student_scores)
student_scores = student_scores.set_index('Student')

print(student_scores.head(3))

print("------")
print(student_scores.describe())

names = student_scores.index
scores = student_scores['Math']

plt.figure(figsize=(8,5))

plt.bar(names,scores, color='skyblue')

plt.title('Score Comparison')
plt.xlabel('Student Name')
plt.ylabel('Score')

plt.show()'''


arrays = np.array([[1,2,3],[4,5,6],[7,8,9]])
col = ['colA','colB','colC']

df = pd.DataFrame(arrays,columns=col)
df['Student'] = ['Studenta','Studentb','Studentc']
df = df.set_index('Student')
print(df)
print('-'*20)

print(df.iloc[0,2])
print('-'*20)
print(df.values)
print(df.index[0])
print(df.columns[0])
print(df.columns.tolist())
print(df.index.tolist())