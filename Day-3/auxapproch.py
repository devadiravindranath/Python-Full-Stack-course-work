'write a code to move all the zeros to the end of the array using a list with extraspace (aux array approach)'

arr=list(map(int,input("enter elements with spaces: ").split()))
result=[]
zeros=0
for num in arr:
    if num !=0:
        result.append(num)
    else:
        zeros+=1
result.extend([0]* zeros)
print("result: ",result)
