a,b = 0,1
n = int(input("enter the nth term: "))
if n == 1:
    print(0)
elif n==2:
    print(0,1)
else:
    print(0,1)
    for i in range(n-2):
        c= a+b
        print(c ,end = ' ' )
        a=b
        b=c