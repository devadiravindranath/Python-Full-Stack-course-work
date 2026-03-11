'''sizes = ('s','mw','xl','xxl','xxxl')
for s in sizes:
    print(f'----|{s}|---')'''

'''followers = ('ravi','dileep','uday','vickey','pavan')
for i in followers:
    print(f'|{i}|follow back|message')'''

'''data = {
    'dileep':['eating','sleeping','talking too much'],
    'ravi':['eating','sleeping','reading'],
    'pavan':['eating','sleeping','walking']
    }
for i in data:
    print(f"{i}:{data[i]}")'''

'''r='Dileep'
for i in r:
    print(i)'''

#range (start,stop+1,step)=range(0,n,1)
'''for i in range(1,21):
    print(i)'''
'''for i in range(0,22,2):
    print(i)'''

'''n= int(input("enter the number: "))
print(f"{n}-Table")
       
for i in range(0,11):
    print(f"{n}*{i}={n*i}")'''
#break
"""for i  in range (0,20):
    if i==5:
        break
    print(i)"""
#continue

"""for i  in range (5,20):
    if i==5:
        continue
    print(i)"""

#while
"""i=1
while i<=10:
    print(i)
    i=i+1"""


"""moves= 20
winning_point=int(input("tell me how many moves is required is required to win: "))
while moves>=1:
    if 20 - winning_point==moves:
        print("you won the match")
        break
    print(f"{moves} are left")
    moves-=1
else:
    print("game over")"""

bullets = 10
while bullets>0:
    print(f"you have{bullets}, bullets shoot them!!")
    bullets-=1

else:
    print("game over")






    
