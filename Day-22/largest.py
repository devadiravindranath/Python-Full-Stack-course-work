import csv

def largest(inp1, inp2, inp3):
    if inp1 >= inp2 and inp1 >= inp3:
        return inp1
    elif inp2 >= inp1 and inp2 >= inp3:
        return inp2
    else:
        return inp3
    
with open("largesttc.csv","r") as file:
     reader = csv.DictReader(file)
     for row in reader:
    
            if largest(int(row['inp1']), int(row['inp2']), int(row['inp3'])) == int(row['output']):
                print("Test Case is passed for", row['inp1'], row['inp2'], row['inp3'])
            else:
                print("Test Case is Failed for", row['inp1'], row['inp2'], row['inp3'])
     
     

         
       
