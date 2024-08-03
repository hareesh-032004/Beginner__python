Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#if you want to accessing the data by using key then we are using dictionary
#-- Dictionary uses key and value pair
#key and value
data={1:'Naresh',2:'Hareesh',4:'Srikanth'}
data
{1: 'Naresh', 2: 'Hareesh', 4: 'Srikanth'}
# here we can use key values to call a particular data
data[2]
'Hareesh'
data[1]
'Naresh'
data[3]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    data[3]
KeyError: 3
# we got an error because we dont have that key value
# here we can use so many in-built functions like clear,copy,get,items,keys,pop,update etc are there
data.get(1)
'Naresh'
data.get(3)
# here we did not got an error
print(data.get(3))
None
#here if we write like this
data.get(1,'Not found')
'Naresh'
# here we have a key of 1: so its is printed
data.get(3,'Not found')
'Not found'
# so here we dont have a key so thats why its is printed not found like supose if we open goolge if page is not working its will tell us not found insterad of the blank page write

keys=['Naresh','Hareesh','Nani']
values=['Java','python','web dev']
# if we print it we get like this
print(keys,values)
['Naresh', 'Hareesh', 'Nani'] ['Java', 'python', 'web dev']
# here i want to coimbine it so lets do it like a dictionary

data=dict(zip(keys,values))
data
{'Naresh': 'Java', 'Hareesh': 'python', 'Nani': 'web dev'}
# so like this we can merge two lists into a dictionary

# ho to add a data in before dictionary
data['Nani']
'web dev'
data['Naveen raj']
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    data['Naveen raj']
KeyError: 'Naveen raj'
# so before we dont have this name so we got an error so define it
data['Naveen raj']='Machine learning'
data
{'Naresh': 'Java', 'Hareesh': 'python', 'Nani': 'web dev', 'Naveen raj': 'Machine learning'}


# if we want to delete value how see it
del data['Nani']
data
{'Naresh': 'Java', 'Hareesh': 'python', 'Naveen raj': 'Machine learning'}








>>> 
>>> 
>>> # creating a new dictionary  with lists and dictionarys
>>> prog={'JS':'Atom','Cs':'VS','python':['pycham','sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
>>> prog
{'JS': 'Atom', 'Cs': 'VS', 'python': ['pycham', 'sublime'], 'Java': {'JSE': 'Netbeans', 'JEE': 'Eclipse'}}
>>> # so here we can know which ide by programmer is working see it
>>> prog[cs]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    prog[cs]
NameError: name 'cs' is not defined
>>> prog['cs']
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    prog['cs']
KeyError: 'cs'
>>> prog['Cs']
'VS'
>>> prog['python']
['pycham', 'sublime']
>>> prog['Java']
{'JSE': 'Netbeans', 'JEE': 'Eclipse'}
>>> prog['JS']
'Atom'
>>> 

>>> # we can use by index number also
>>> prog['python'][0]
'pycham'
>>> prog['Java'][1]
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    prog['Java'][1]
KeyError: 1
>>> # here we should menction the key value*******
>>> prog['Java']['JEE']
'Eclipse'
