import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

#rng = np.random.RandomState(30)

'''ages = {}
ages['Age'] = rng.randint(22,51,30)
bought_insurance = {}
bought_insurance['Bought_Insurance'] =  rng.randint(0,2,30)'''


'''df = pd.DataFrame({
    'Age': ages['Age'], 
    'Bought_Insurance': bought_insurance['Bought_Insurance']
})'''
'''ages.update(bought_insurance)

df = pd.DataFrame(ages)'''
df = pd.DataFrame({
    'Age': [22, 25, 47, 52, 46, 56, 55, 60, 62, 61, 18, 28, 27, 29, 49,None],
    'Bought_Insurance': [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1,1]
})


X = df[['Age']]
y = df['Bought_Insurance']

model  = LogisticRegression()
model.fit(X,y)
#model.fit(X.values,y)
age = int(input("Age input : "))
prediction_data = pd.DataFrame([[age]],columns=['Age'])
print(prediction_data)
#print(f"อายุ 50: {model.predict([[50]])[0]}")
print(f"อายุ {age}: {model.predict(prediction_data)[0]}")
print(f"ความน่าจะเป็นของคนอายุ {age}: {model.predict_proba(prediction_data)}")