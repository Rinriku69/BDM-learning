
print([item for item in "Hello"])
print([item*2 for item in [1,2,3]])
print([i+j for i in [1,2,3] for j in [1,2,3 ]])
print([item for item in []])

print( [item for item in [1, 2, 3] if item == 1])

print([item*2 for item in "Hello"])
print([i*item for i,item in enumerate([1,2,3])])
print({item:item*2 for item in [1, 2, 3]})
print({i:j for i in "Hello" for j in [1,2,3]}) #nested loop 
'''for i in "Hello":
    for j in [1, 2, 3]:
        dict[i] = j'''



a = {
    'name': "Jacob",
    'age': 24
}

for key,value in a.items():
    print(f"{key} :{value}")
    
    
