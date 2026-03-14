'''print('STUDENT INFORMATION')
def student_data(info):
    print(f'Name: {info[0]}')
    print(f'course: {info[1]}')
    print(f'Graduation year: {info[2]}')
    print('------end------')


data=[['pavan','PFS','2025'],
      ['nani','JFS','2024'],
      ['dileep','MERN','2065'],
      ['ravi','PFS','2026'],  
      ]
for i in data:
    student_data(i)'''
#positional arguments the values are passed in order 
'''def display(username,email,password):
    print(f'Username:{username}')
    print(f'Email:{email}')
    print(f'Password:{password}')
    print('\n\n')

display('dileep','dileep@gamil.com','dddd1234')'''


#keyword argument the name should equal to the value

'''def display(username,email,password):
    print(f'Username:{username}')
    print(f'Email:{email}')
    print(f'Password:{password}')
    print('\n\n')

display(username='dileep',email='dileep@gamil.com',password='dddd1234')'''

#default argument is a function argument that already has a value,
#and that value is used if no argument is passed while calling the function

"""def display(username,email,password,status='absent'):
    print(f'Username:{username}')
    print(f'Email:{email}')
    print(f'Password:{password}')
    print(f'Status:{status}')
    print('\n\n')

display('dileep','dileep@gamil.com','dddd1234','present')"""


#variable length arguments: Used when number of arguments is unknown
def display(*names):
    for i in names:
       print(i)
    else:
        print('--end of the list---')

display('dileep')
display('pavan','saaketh','ravi')
display('nani','jhony')




    
