#Recursion in python::

#recursion means calling the same function itself:
def greet():
    print('Hello')  
    #greet()#if we keep the function call inside the function then it will repedally call by itself and it will give infinite times but in python it will execuete only 1000 times only
greet()    


# if you want to know about the limit of the recurssion then import sys and us the function
import sys
sys.setrecursionlimit(2000)#here we can increase the limit also
print(sys.getrecursionlimit())
i=0
def greet():
    global i
    i=i+1
    print('Hello')  
    greet()
greet()




#factorial using the Recursion::.
def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)
x=int(input('Enter the value of your number:'))
result=fact(5)
print('The factorial of the your number is:',result)


