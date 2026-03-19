"""n= int(input("enter the number: "))
for rows in range(n):          
    for col in range(n):
        print(col,end=' ')
    print()"""

"""n= int(input("enter the number: "))
num=1
for rows in range(n):          
    for col in ran8ge(n):
        print(num,end=' ')
        num+=1
    print()"""

"""n= int(input("enter the number: "))
for rows in range(n):          
    for col in range(n):
        print(rows+col,end=' ')
    print()"""


"""n= int(input("enter the number: "))
for rows in range(n):          
    for col in range(n):
        if (rows+col)%2==0:
            print(0,end=' ')
        else:
            print("x",end=' ')
    print()"""
"""n= int(input("enter the number: "))
for rows in range(n):          
    for col in range(rows+1):
        print('*',end=" ")
    print()"""
"""n= int(input("enter the number: "))
for rows in range(n):          
    for col in range(n-rows):
        print('*',end=" ")
    print()"""
"""n= int(input("enter the number: "))
for rows in range(n):
    for spc in range(rows+1):
        print(' ',end=' ')
    for col in range(n-rows):
        print('*',end=' ')
           
    print()"""
n= int(input("enter the number: "))
for rows in range(n*2):
    if rows<=n:
        print('*'*(rows+1))
    else:
        print('*'*(2*n-rows+1))
    
