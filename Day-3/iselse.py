products = ['shirts','T-shrts','watches','slippers']

search= input("enter the item: ")

if search in products:
    print(f'{search} is found!!\nGO and shop now!!')
else:
     print(f'{search} is not found!!\nlook for the other things !!')
