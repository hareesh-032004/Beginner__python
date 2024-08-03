#Zip Function in Python::

names=['Naresh','Haressh','Vinay','Srikanth']

coms=['google','Amazon','facebook','Instgram']


data=list(zip(names,coms))#ordered
data1=set(zip(names,coms))#unordered
data2=dict(zip(names,coms))
data3=zip(names,coms)
print(data)
print(data1)
print(data2)

#we can also do it by for loop::

for (a,b) in data3:
    print(a,b)
