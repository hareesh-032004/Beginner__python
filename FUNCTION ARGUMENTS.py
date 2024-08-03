#Function Arguments in Python:
def update(x): # so here we havinf a function called update and argument or variable x
    x=8
    print(x)
update(20)

#if you want to
def update(x):
     x=8
     print('x',x)

a=10    
update(a)
print('a',a)


#when ever you pass a value to call a function by passing a value they will share the same the same ID, the variable which has been passed and the variable you are assecsing it here but then the moment you change the value it will change the address again
#In python we dont use the callby value and call by reference

def update(x):
    print(id(x))
    x=8
    print(id(x))
    print('x',x)

a=10
print(id(a))
update(a)
print('a',a)



#with list
def update(lst):
    print(id(lst))
    lst[1]=25
    print(id(lst))
    print('x',lst)

lst=[10,20,30]
print(id(lst))
update(lst)
print('lst',lst)


