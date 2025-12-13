from random import shuffle
import random


check = []
counter = 0
tried = 0
while check.count(0) < 10 :
 check = []
 for i in range(10):
    ran1 = random.randint(1,2)
    ran2 = random.randint(1,2)
    if ran1 == ran2:
        check.append(1)
    else:
        check.append(0)
 counter += 1
 tried += 1
 """ if counter >= 10:
     counter = 0
     continue """



print(tried)
print(counter)
failed_chance = 1-(0.5**10)

print(f"The chance of getting in {counter} attemt : {(1-failed_chance**counter)*100}%")

