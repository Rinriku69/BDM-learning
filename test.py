""" print("Age Calculation")

birthYear = input("Your Birth Year : ")

age = 2025-int(birthYear)


print(f"Your age is {age} Your birth year is {birthYear}" )

if age < 20:
    print("You are a Teenager")
else:
    print("You are an Adult") """

""" customer_ages = [18,20,31,15,40]

for i in range(len(customer_ages)):
    print(f"Customer {i+1} Age: {customer_ages[i]}")

    if customer_ages[i] < 20:
        print("-> Status :Teenager")
    else:
        print("-> Status :Adult")

a = 5//2
print(a) """

""" a = int(input("Please input A = "))
b = int(input("Please input B = "))
print(f"Result of A + B is {a+b}") """

""" pi = '.141592653589793238462643383279502884197169399375105'

digit = int(input("pi digit number = "))
print("3" + pi[0:digit])
print(len(pi)) """

""" a = " Hello World"

print(a*3) """

""" fruits = ["apple "," banana","kiwi "]
b = fruits[1].split("a")
print(b)

for i in range(len(fruits)):
    print(fruits[i].strip().upper()) """

""" a = {"James" : 52, "Kevin" : 64}

for key, value in a.items():
    print(f"Name : {key}, Age :{value}") """

""" student = {"id": "35654",
           "name": "Sirithep",
           "score" : 82}
student['score'] = 90
student['grade'] = "A"
for key in student:
    print(f"{key} : {student[key]}") """


""" all_student = []

def grading(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

for i in range(2):
    name = input("Input Name : ").strip()
    score = float(input("Input Score : ").strip())
    student={}
    student["name"] = name
    student["score"] = score
    student["grade"] = grading(score)

    all_student.append(student)

print(all_student)

for s in all_student:
    print(f"{s['name']} : {s['grade']}") """



