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

'''plt.scatter(df['Hours_Study'],df['Exam_Result'], color='red', alpha=0.5)
plt.title('Hours Study and Exam result')
plt.xlabel('Hours Study')
plt.ylabel('Exam Result')
plt.show()'''

rng = np.random.RandomState(0)
x = sorted(rng.randint(1,11,10))
y = rng.randint(1,11,10)


'''plt.figure("X & Y figure",figsize=(8,5))
plt.plot(x,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("X & Y")
plt.grid()
plt.show()'''

plt.subplot(1,2,1)
plt.bar(x,y,0.4,label='Female')

x = np.array(x)+1
tick = [1,2,3,4,5,6,7,8,9,10]

plt.subplot(1,2,2)
plt.bar(x,y,0.4,color='red',label='Male')
plt.legend(loc ='upper right')
print(y)
plt.xticks(tick,y,rotation=45)
plt.show()
