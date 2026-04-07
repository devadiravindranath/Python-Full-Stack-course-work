s ='abid is good boy'

res = ' '
cur = ' '

for i in s:
    if i in cur:
        if len(cur)>len(res):
            res=cur
        cur =i
    else:
        cur+=i

if len(cur)>len(res):
     print(cur)
else:
    print(res)