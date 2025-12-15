""" import pandas as pd
import numpy as np
import random

#np.random.seed(30)

hp = np.random.randint(59,200)
atk = np.random.randint(10,101)


def status_generator(name):
    pokemon = {}
    
    hp = np.random.randint(59,200)
    atk = np.random.randint(10,101)
    pokemon[name] = {
        'hp': hp,
        'atk': atk
    }
 
    return pokemon

poke_dex = []
for i in range(10):
    pokemon_name = f"a{i}"
    pokemon = status_generator(pokemon_name)
    poke_dex.append(pokemon)

clean_row = []
for item in poke_dex:
    for key, value in item.items():
        new_rows=value.copy()
        new_rows['name'] = key
        clean_row.append(new_rows)

df = pd.DataFrame(clean_row)

df =df[['name','hp','atk']]

print(df)
print("-"*15+"Poke Battle!"+"-"*15)

pair = []
pair = random.sample(clean_row,2)

A = {}
A = pair[0]
B = {}
B = pair[1]
    
print(A)
print(B)

while A['hp'] | B['hp'] > 0:
    A['hp'] = A['hp'] - B['atk'] 
    B['hp'] = B['hp'] - A['atk'] 
    print(f"{A['name']}'s Hp :{A['hp']}")
    print(f"{B['name']}'s HP :{B['hp']}")
    if(A['hp'] <= 0):
        winner = B
    else:
        winner = A
        
print(f"Winner is {winner['name']}")
 """
""" import numpy as np
 
rng = np.random.RandomState(0)
pokemon = rng.choice(
    ["🐣 Pichu", "🔥 Charmander", "🌿 Bulbasaur", "💧 Squirtle", "🦇 Zubat"],
    size=(3, 4)
)

print(pokemon)
print(f"\nCaught at (1,2) : {pokemon[1,2]}")
print(f"Last Column : {pokemon[:,-1]}")

print(f"First two rows: {pokemon[0:2,:]}")

print(f"Number of 🔥 Charmander: {(pokemon == "🔥 Charmander").sum()}")

print(f"All 💧 Squirtle: {pokemon[pokemon == "💧 Squirtle"]}") """

 
import numpy as np
import pandas as pd

rng = np.random.RandomState(0)
products = np.array(["Laptop", "Phone", "Tablet", "Camera"])
branches = np.array(["North", "South", "East", "West"])



profits = rng.randint(-10, 40, size=(4, 4))
df = pd.DataFrame(profits,index=products,columns=branches)
print(df)
#profits[2,1] = 13
#profits[3,1] = 25
print(profits)
print(f"Product of the day is {''.join(rng.choice(products,1))}")


print(f"High-profit products : {' '.join(products[[i for i in range(profits.shape[0]) if np.max(profits[i,:]) >= 25]])}") 

print(f"Weak branches : {' '.join(branches[[i for i in range(profits.shape[1]) if np.average(profits[:,i]) < 5]])}")

new_profit = np.delete(profits,[i for i in range(profits.shape[1]) if np.average(profits[:,i]) < 5],axis=1)
print(f"Matrix without weak branches: \n{new_profit}") 
 
#profits[3,1] = -50

print(f"Negative trend products: \n{' '.join(products[[i for i in range(profits.shape[0]) if np.sum(profits[i,:]) < 0]])}")

""" weights = [50, 68, 90]
heights = [1.60, 1.75, 1.70]
wh = zip(weights,heights)


def bmi(weight, height):
    value = weight / (height ** 2)
    if value < 18.5:
        status = "Underweight"
    elif value < 25:
        status = "Normal"
    elif value < 30:
        status = "Overweight"
    else:
        status = "Obese"
    return value, status

def bmi_cal(wh):
    
    return [str(round(w/(h**2),2))+'->Obese' if w/(h**2)>=30 else str(round(w/(h**2),2))+'->Overweight' if w/(h**2)>=25 else str(round(w/(h**2),2))+'->Normal' if w/(h**2) >= 18.5 else str(round(w/(h**2),2))+'->Underweight' for w,h in wh] 

#print('\n'.join(['student '+str(i+1)+': '+str(v) for i,v in enumerate(bmi_cal(wh))]))
 
print('\n'.join([
    f"Student {i+1}: BMI {round(v, 2)} -> {s}"
    for i, (w, h) in enumerate(zip(weights, heights))
    for v, s in [bmi(w, h)]
])) """