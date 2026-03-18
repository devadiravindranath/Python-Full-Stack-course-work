"""with open('sample1.txt','w') as file:
    file.write("hello world")"""
"""with open('sample1.txt','a') as file:
    file.write("override")"""

"""import csv
with open('sample2.csv','r') as file:
    data = csv.reader(file)

    for row in data:
        print(row)"""

"""import csv

with open('sample222.csv','w',newline='') as file:
    data=csv.writer(file)
    data.writerow(['Product_ids','product','price'])
    data.writerow(['1','chocolate','20'])
    data.writerow(['2','milk','30'])
    data.writerow(['3','biscuit','10'])"""

"""import csv
with open('sample222.csv','r') as file:
    data=csv.reader(file)
    for i in data:
        print(i)"""
import json

with open('demo.json','w') as file:
    data=[
	{'id':'1','name':'saaketh'},
	{'id':'2','name':'dileep'},
	{'id':'3','name':'vicky'},
        ]
        json.dump(data,file,indent=4)
        print("Data saved successfully")
