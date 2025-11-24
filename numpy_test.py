import numpy as np
import pandas as pd


""" raw_data = np.random.randint(0,100, size=(5,3))

print(raw_data)

subjects = ['Math', 'Science', 'English']
students = ['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5']

student_score = pd.DataFrame(raw_data,students,subjects)
print(student_score)
print("-Math score-")
print(student_score['Math']) """

""" data_dict = {
    'Math': [80, 60],
    'Science': [75, 50],
    'English': [90, 40]
}

df_dict = pd.DataFrame(data_dict, index=['Student A', 'Student B'])

print("\n--- From Dictionary ---")
print(df_dict) """



""" data_list = [
    [80, 75, 90],
    [60, 50, 40]
]
cols = ['Math', 'Science', 'English']
df = pd.DataFrame(data_list, columns=cols)

print("--- From Python List ---")
print(df) """
