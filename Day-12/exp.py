"""students= {
    "vicky":80,
    "nani":70,
    "uday":90
    }
try:
    name=input("Enter student name: ")
    print("Marks:",students[name])

except KeyError:
    print("student not found")"""



"""
set1=set(map(int,input("enter first set elements: ").split()))
set2=set(map(int,input("enter second set elemnets: ").split()))

print("union:", set1 | set2)
print("intersection:",set1 & set2)
print("difference", set1 - set2)"""

"""try:
    with open("sample1.txt","r") as f:
        lines = f.readlines()
        print("file contens: ")
        for line in lines:
            print(line,end="")
        print("\n number of lines:",len(lines))
except FileNotFoundError:
    print("File not Found")"""


import json

students={
    "name":"ravi",
    "age":20,
    "marks":90
    }
with open("students.json","w") as f:
    json.dump(students,f)

with open("students.json","r") as f:
    data=json.load(f)
    print(data)







































