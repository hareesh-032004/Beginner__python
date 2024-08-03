#Array in python::
#in arrays we need all the values of the same type:
#here we have so many tyeps of improting array they are
#import array
#import array as arr
#from array import * means all modules

from array import *
vals=array('i',[5,-89,8,4,2]) #here we are using the 'i' means int of size 2 if we keep the float values we will get an error.. and  we can put the -ve values also. and if we keep the 'I' then we get an error because it is an unsingned integer so in quetsion we kept the negitive value
print(vals)




#if we want to print the address and that size then use the buffer_info()
from array import *
vals=array('i',[5,-9,8,4,2])
print(vals.buffer_info())  #output is (1468124558448->address, 5->size)

#we have so many methods if we want print the which type then use typecode.
from array import *
vals=array('I',[10,20,34,5,6,78])
print(vals.typecode)
#and we have so many methods like append,remove,reverse, etc..

#reverse:
from array import *
vals=array('I',[10,20,34,5,6,78])
vals.reverse()
print(vals)

#index:
from array import *
vals=array('I',[10,20,34,5,6,78])
print(vals[3])


#so in index we want all numbers then we can do like this
from array import *
vals=array('I',[10,20,34,5,6,78])
for i in range(len(vals)):
    print(vals[i])



#here we can do without using the range
from array import *
vals=array('i',[23,4,55,66,778,99])
for e in vals:
    print(e)



#here we can work with also 'char'
from array import *
ch=array('u',['N','a','r','e','s','h'])
for i in ch:
    print(i)



#if we create a new value then we can get vales from before list
from array import *
vals=array('i',[23,45,56,77,72,30])
newArr=array(vals.typecode,(a*a for a in vals))
for e in newArr:
    print(e)




#write a code to sort the array in asending the order::
from array import *
arr=array('i',[12,5,76,89,23,67,85,90])
arr=sorted(arr)
for i in arr:
    print(i)
    
    
#write a code to find the factorial of the given number:
num=int(input("Enter the number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("The factorial is:",fact)    
    
