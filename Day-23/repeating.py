s = 'pythonpython'

for i in s:
    if s.count(i) == 1:
        print("first non-repeating character: ",i)
        break
else:
    print("all character are repeated")