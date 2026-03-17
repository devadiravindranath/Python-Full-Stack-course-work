import csv

with open("sample.csv",'w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['5','abid','python'])
