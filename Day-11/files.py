"""file = open('sample.txt','r')

content1 = file.read()
file.seek(0)
content2 = file.readline()
file.seek(0)
content3=file.readlines()
print(content1,content2,content3,sep='\n\n')

file.close"""

file = open('sample.txt','w')

file.write("hellow dileep")

file.close
