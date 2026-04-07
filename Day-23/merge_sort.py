list1 = [30, 50, 90, 120]
list2 = [10, 20, 40, 60, 70, 130, 190, 200]

i = 0
j = 0
res = []

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        res.append(list1[i])
        i += 1
    else:
        res.append(list2[j])
        j += 1

# add remaining elements
if i < len(list1):
    res.extend(list1[i:])

if j < len(list2):
    res.extend(list2[j:])

print(res)