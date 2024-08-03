#Global Keyword in Python | Global vs Local Variable:
a=10 #This is called Global variable
def something():
    a=20#this is called local variable
    print('Local variable:',a)
    
something()
print('Global variable:',a)



#here is there trick
a=10
def something1():
    global a #if we use global keyword here then it will not print the 10 outside one 
    a=15
    print('Local:',a)
    
something1()
print('outside',a)



#
a=10
print(id(a))

def something():
    a=9

    x=globals()['a']
    print(id(x))
    print('Local:',a)
    globals()['a']=15

something()
print('outside:',a)

    
