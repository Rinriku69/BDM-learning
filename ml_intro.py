import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(30)

hours = np.random.randint(1,11, size=100)

scores = []

for h in hours:
    chance = h * 10
    score = (np.random.randint(0,100) + chance) /2
    scores.append(score)



df = pd.DataFrame({
    'Hours_Study':hours,
    'Exam_Result': scores
})

""" print(df.head(10)) """

plt.scatter(df['Hours_Study'],df['Exam_Result'], color='red', alpha=0.5)
plt.title('Hours Study and Exam result')
plt.xlabel('Hours Study')
plt.ylabel('Exam Result')
plt.show()