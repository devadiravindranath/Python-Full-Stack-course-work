"""n= {"Arjun":85,"Rahul":90,"anitha":78}
name = input("Enter student name: ").strip()
try:
    print(n[name])

except KeyError:
    print("Student not found")"""


"""s1 = set(map(int,input("enter set1: ").split()))
s2 = set(map(int,input("enter set1: ").split()))

print(f"Union: {s1 | s2 }")
print(f"intersection: {s1 & s2 }")
print(f"Difference: {s1 - s2 }")"""

"""try:
    with open("data.txt","r") as file:
        print(len(file.readlines()))

except FileNotFoundError:
    print("data.txt does not exist")"""

import json

with open('demo1.json','w') as file:
    data = [
        {'title': 'py','author':'abc','price':123},
        {'title': 'java','author':'abvb','price':1230},
        {'title': 'sd','author':'adg','price':163},
        {'title': 'ds','author':'fggh','price':1256}
        

        ]

    json.dump(data,file,indent=4)

with open('demo1.json','r') as file:
    print(json.load(file))

