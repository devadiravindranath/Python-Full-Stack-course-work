def add(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def mod(a,b):
    return a%b
exp = str(input("Enter the expression: "))
print(exp)

for i in exp:
    if i=='+':
        a,b=exp.split('+')
        print(add(int(a),int(b)))
    elif i=='-':
        a,b=exp.split('-')
        print(subtraction(int(a),int(b)))
    elif i=='*':
        a,b=exp.split('*')
        print(multiplication(int(a),int(b)))
    elif i=='/':
        a,b=exp.split('/')
        print(division(int(a),int(b)))
    elif i=='%':
        a,b=exp.split('%')
        print(mod(int(a),int(b)))
    
        
        
