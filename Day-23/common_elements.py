list1 = [30,40,55,60,70,80]
list2 = [40,50,90,100]

res = []
for i in list1:
    if i in list2:
        res.append(i)

print(res)