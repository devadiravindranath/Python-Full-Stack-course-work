arr = list(map(int,input("enter number with space: :").split()))
unique=[]
for i in arr:
    if i not in unique:
        unique.append(i)
print("list after removing duplicate:",unique)
