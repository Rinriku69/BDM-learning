'''num =[]
for i in range(3):
    inputs = int(input(f"Score {i+1} = "))
    num.append(inputs)

Average = sum(num)/len(num)

print(round(Average,2))'''

'''inputs = input("Input : ")

ninputs = inputs.split('|')
ordered_in = []
ordered_in.append(ninputs[2])
ordered_in.append(ninputs[1])
ordered_in.append(ninputs[0])

print(' -- '.join(ordered_in))
print('ME' in ninputs[2])'''

'''content = "volcano ash magma lava".replace('lava','🔥')
split_content = content.split(' ')
lava_position = content.find('🔥')

print('..'*int(len(split_content)-1) + str(content[lava_position]))'''

'''content = "noise..noise..START_Target_is_at_the_Casino_Royale_END..noise.."

print(' '.join(content[content.find('START'):content.find('END')].split('_')).replace('START','').replace('Casino','[CLASSIFIED]')
)'''

'''content = "[INV-1001]: 5 units @ $1,500.00".split(' ')
print(int(content[1]) * float(content[-1].replace('$','').replace(',',''))
)'''

'''catalog = {'A101': 'Laptop Pro,20000', 'B205': 'Mouse Wireless', 'C310,100': 'Monitor 27-inch,5000'}

inputs = "LOC:WH03-CODE-A101-QTY:5".split('-')

code = inputs[inputs.index('CODE')+1]

product = catalog[code].split(',')[0]
price = catalog[code].split(',')[1]
total = int(price) * int(inputs[-1].split(':')[1])

qty_string = next(item for item in inputs if 'QTY' in item)
qty = qty_string.split(':')[1]
print(qty)

print(f"Product Name : {product}, Total Price : {total}")'''

'''students = {'S01': 'Alice', 'S02': 'Bob', 'S03': 'Charlie'}

students['S01'] = [students['S01'],int(input(f"S01:"))]
students['S02'] = [students['S02'],int(input(f"S02:"))]
students['S03'] = [students['S03'],int(input(f"S03:"))]

print("--- Student Score Bar Chart ---")
print(students['S01'][0]+" (S01) :"+"*"*int(students['S01'][1]/5))
print(students['S02'][0]+" (S02) :"+"*"*int(students['S02'][1]/5))
print(students['S03'][0]+" (S03) :"+"*"*int(students['S03'][1]/5))

for i in range(3):
    students[f'S0{i+1}'] = [students[f'S0{i+1}'],int(input(f"S0{i+1}:"))]
print("--- Student Score Bar Chart ---")
for key, value in students.items():
    print(students[key][0]+" (S01) :"+"*"*int(students[key][1]/10) + f"({students[key][1]})")'''
    
'''students = {'S01': 'Alice', 'S02': 'Bob', 'S03': 'Charlie'}

for i in range(3):
    students[f'S0{i+1}'] = [students[f'S0{i+1}'],int(input(f"S0{i+1}:"))]
print("--- Student Score Bar Chart ---")
print(sorted(students))
test_func = lambda x: x[1]
print([test_func(item) for item in students.values()])'''

'''n = int(input("n = "))

#for i in range(n):
    #print("*"*(i+1))
      
for i in range(n):          
    for j in range(i + 1): 
        print("*", end="")  
    print()'''
    
    
'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
moded = []
for i in numbers:
    moded.append(i%2)
    
print(f"Even:{moded.count(0)}")
print(f"Odd:{moded.count(1)}")'''
