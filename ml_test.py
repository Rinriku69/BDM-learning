import pandas as pd
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
