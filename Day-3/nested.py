data = {
    'pavan': { 'status':True,'python':100,'mysql':90,'skills':80 },
    'dileep': { 'status':False,'python':None,'mysql':None,'skills':None },
    'ravi': { 'status':True,'python':80,'mysql':70,'skills':99 },
     'saaketh': { 'status':True,'python':55,'mysql':45,'skills':65 },
     'vickey': { 'status':True,'python':20,'mysql':30,'skills':25 }
    }
user= input("Enter the student name: ")

if user in data:
    if data[user]['status']:
        sum =data[user]['status']+data[user]['mysql']+data[user]['skills']
        avg=sum/3
        if avg > 70:
             print(f"congrats {user} !!!! \nyou got 'A' grade")
        elif avg > 50:
             print(f"better {user} !!!! \nyou got 'B' grade")
        elif avg > 40:
             print(f"average {user} !!!! \nyou got 'c' grade")
        else:
             print(f" {user},failed in the exam !!!! \nyou got 'f' grade")
    else:
             print(f" {user},did not write any exam !!!!")
else:
             print(f" {user},user not found!!!!")
            
