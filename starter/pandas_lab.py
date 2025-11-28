import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

student_scores = pd.read_csv('student_score.csv')
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

plt.show()