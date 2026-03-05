'''write a code to count the recuring freq of numbers in an array  using hashing or dict approach'''

arr=list(map(int,input("enter elements wiith spaces ").split()))
freq={}
for num in arr:
    freq[num]= freq.get(num,0)+1
for k,v in freq.items():
    print(k,"->",v)
