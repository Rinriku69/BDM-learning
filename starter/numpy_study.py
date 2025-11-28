import numpy as np
import pandas as pd


raw_data = np.random.randint(0,100, size=(5,3))

print(raw_data)

subjects = ['Math', 'Science', 'English']
students = ['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5']

student_score = pd.DataFrame(raw_data,students,subjects)
print(student_score)
print("-Math score-")
print(student_score['Math'])

data_dict = {
    'Math': [80, 60],
    'Science': [75, 50],
    'English': [90, 40]
}

df_dict = pd.DataFrame(data_dict, index=['Student A', 'Student B'])

print("\n--- From Dictionary ---")
print(df_dict)



data_list = [
    [80, 75, 90],
    [60, 50, 40]
]
cols = ['Math', 'Science', 'English']
df = pd.DataFrame(data_list, columns=cols)

print("--- From Python List ---")
print(df)


L1 = [1,2,3,4,5]
L2 = [4,5,6,7,8]
V = np.array([L1,L2])
#print(V[:,[0,2]])  

rng = np.random.RandomState(2)
metrix =rng.randint(1,4,(5,3))
#metrix = np.delete(metrix,1,axis=0)
print(metrix)

rows, cols  = np.where(metrix == 1)



print([str(row)+str(cols[i]) for i,row in enumerate(rows)])
one = metrix == 1
print(one.sum(axis=0))
#print(rng.choice(range(1,5),6,replace=True))
