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


'''arrays = np.array([1,2,3])
lists = [1,2,3]
col = ['colA','colB','colC']

df = pd.DataFrame({'H1':lists
                   ,'H2':lists})'''
'''df['Student'] = ['Studenta','Studentb','Studentc']
df = df.set_index('Student')'''
#print(df.set_index('H1'))
'''print('-'*20)

print(df.iloc[0,2])
print('-'*20)
print(df.values)
print(df.index[0])
print(df.columns[0])
print(df.columns.tolist())
print(df.index.tolist())'''

df = pd.DataFrame({
    'Age': [22, 25, 47, 52, 46, 56, 55, 60, 62, 61, 18, 28, 27, 29, 49,None],
    'Bought_Insurance': [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1,1],
    'Status':['Alive','Alive','Unalive','Unalive','Alive','Unalive','Unalive','Unalive','Alive','Unalive','Alive','Alive','Alive','Alive','Alive','Alive']
})
#print(df.groupby('Bought_Insurance').size()) #แต่ละvalue มีกี่ตัว
#print(df.groupby('Bought_Insurance').count()) #ในแต่ละcolumn มีกี่แถวที่มีvalue ตาม/group by bought_insurance
#print(df.groupby('Bought_Insurance').mean()) #ค่าเฉลี่ยของแต่ละcolumn ตามvalue ของ bought_insurance
#print(df.corr(method='pearson')) #หาสัมประสิทธิ์สหสัมพันธ์
#print(df.isnull().sum(1)) #sum(1)เพื่อดูว่าแต่ละแถวมีข้อมูลที่หายไปกี่column
#print(df.isnull().sum()) #แต่ละcolumn มีข้อมูลหายไปกี่แถว

#df_clean = df.dropna() #ลบแถว/index ที่ข้อมูลไม่ครบ
#print(str(df.shape) + str(df_clean.shape))
#df_clean = df.dropna(axis=1) #ลบcolumnที่มีค่าว่าง
#df.columns[(df.isnull().sum()>0)] #คอลลัมที่มีค่าnullมากกว่า0
#df.index[(df.isnull().sum(1)>0)] #แถวที่มีค่าnullมากกว่า0
#print(df.columns[(df.isnull().sum()>0)].tolist()) #list ของcolumnที่มีข้อมูลหายไปมากกว่า...
#df.drop(column_name , axis=1) #ดรอปcolumnได้เลย
#print(df['Age'].unique()) #เพื่อดึงข้อมูลทั้งหมดออกมา โดยเอาตัวซ้ำมาแค่อันเดียว

print(df.dtypes)
result = pd.factorize(df['Status']) #แปลงตัวหนังสือเป็นเลข
df['Status'] = result[0]
print(df['Status'])

del_row = df.index[(df.isnull().sum(1)>0)].tolist()
x = df.dropna()
print(df)
print(x)