# Functions in Python::
#syntax is
def greet():
    print("Hello")
    print("Good Morning")
    
greet()# so here you should call the function then only output will come
#so here the function is used to vall the multiple times in industry they dont write full code again and again if they want they just call the function lets see that

greet()
greet()#you can see the output


#how to add numbers in functions
def add(a,b):
    c=a+b
    print(c)
    
add(5,4)


#so here function is of two types its returns a value and it not return a value
def add(x,y):
    c=x+y
    return c
greet()
result=add(5,4)
print(result)



#from the function you can return the multiple values::
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
result1,result2=add_sub(5,4)
print(result1,result2)


#imp point function is block where you will have one task,so if you want to achive one task,write a function to that so it's better to write a code individulayy so that we can modify for that function in futute not the entire code
