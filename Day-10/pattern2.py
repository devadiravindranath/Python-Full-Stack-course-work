"""n= int(input("enter the number: "))
for rows in range(n):
    for col in range(n):
        if rows==0 or col==0 or rows==n-1 or col==n-1 or rows==n//2 or col==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()"""

"""n= int(input("enter the number: "))
for rows in range(n):
    for col in range(n):
        if rows==0 or   rows==n-1 or rows+col==n-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()"""

n= int(input("enter the number: "))
for rows in range(n):
    for col in range(n):
        if rows==col or rows+col==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
