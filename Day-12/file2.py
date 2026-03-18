"""import json

with open('demo.json', 'w') as file:
    data = [
        {'id': '1', 'name': 'saaketh'},
        {'id': '2', 'name': 'dileep'},
        {'id': '3', 'name': 'vicky'}
    ]

    json.dump(data, file, indent=4)

print("Data saved successfully")"""
import json

with open('demo.json','r') as file:
    data=json.load(file)
data.append({'id':'4','name':'abid'})

with open('demo.json','w') as file:
    json.dump(data,file,indent=4)
