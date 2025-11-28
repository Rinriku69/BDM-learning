import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

np.random.seed(10)

temperature = np.random.randint(25,36,size=30)

sales = (temperature * 5) + np.random.randint(-10,11,size=30)

df = pd.DataFrame({
    'Temperature':temperature,
    'Sales':sales})



#print(df[df['Sales']>160])
print(df.describe())

""" plt.scatter(df['Temperature'],df['Sales'],color='red',alpha=0.5)
plt.title('Temperature and Sale of Iced-Coffe')
plt.xlabel('Temperature')
plt.ylabel('Sales')
plt.show() """

X = df[['Temperature']]
y = df['Sales']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=30 )

print("-"*30)
print(f"Train : {len(X_train)}")
print(f"Test : {len(X_test)}")

model = LinearRegression()

model.fit(X_train,y_train)

y_predict = model.predict(X_test)

compare_df = pd.DataFrame({
    'Temperature': X_test['Temperature'],
    'Actual sale': y_test,
    'Predict sale': y_predict,
    'Diff': y_test - y_predict
})

print(compare_df)

print(f"\nสูตรที่ AI คิดได้: Sales = (Temp * {model.coef_[0]:.2f}) + {model.intercept_:.2f}")