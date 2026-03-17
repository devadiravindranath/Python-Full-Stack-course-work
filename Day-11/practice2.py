"""a=[0,1,0,2,1,0,1,2,0,0,0]
while 0 in a:
    a.remove(0)
print(a)"""
"""a=[0,1,0,0,5,4,0]
a=[x for x in a if x!=0]+[0]*a.count(0)
print(a)"""
"""t=(11,5,5,4,5,)
print(set(t))"""

"""for i in range(5):
    for j in range(5):
        if  j==0 or j==4 or i==2 :
            print("*",end=" ")
        else:
            print(" ",end="")
    print()"""

"""for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4 or i==2:
            print("*",end="")
        else:
            print(" ",end="")
    print()"""
n=int(input("enter the number: "))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
