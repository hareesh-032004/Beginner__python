#if we talk about arrays we have 1D,1D,3D arrays but in python we dont have 2D,3D have but they don't support that so that only for 2D,3D we use the third party package called as the numpy.. so we have to install it
from numpy import *
arr=array([1,2,3,4,5],int) #so here in numpy we don't want to use the type of 'i' if we want to use the then we can put it at the end as int
print(arr)


#ways of creating Arrays in Numpy are::
#array(),linspace(),logspace(),arange(),Zeros(),ones()
from numpy import *
arr=array([1,2,3,4,5,6],float)#we know that in arrays array should be of same type but if we import numpy then it will convert the type to all of them in array and give not an error thats the beuty of numpy... in array we are keeping the integer but type we are giving is float then it will convert by default to float 
print(arr.dtype)
print(arr)


#linespace():means it have an (start,stop,restep)
arr=linspace(0,15)#so it basically converts the 50 float values by default any number 50 parts
arrs=linspace(0,15,16)#so it bacically tell that 16 means how many parts i want to go for
print(arr)
print(arrs)


#arange():means it have an (start,stop,step)
arr=arange(1,100,2)
print(arr)



#logspace():means it is log(start,stop,step)
arr=logspace(1,40,5)
print(arr)
print('%.2f' %arr[4])



#zeros():
arr=zeros(5)
print(arr)

#ones():
arr=ones(5,int)
print(arr)#if we want int then menction it by default it will give float..
