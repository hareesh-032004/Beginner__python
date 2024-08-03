from numpy import *
arr1=array([
             [1,2,3,4,5,6],
             [7,8,9,10,11,12],
             [13,14,15,16,17,18]
    ])
#if we want to convert the 2d to 1d then use the flaten() function
arr2=arr1.flatten()
arr3=arr2.reshape(3,3,2) #conevrt 1d to 2d
print(arr3)
print(arr2)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)#3x3


from numpy import *
arr4=array([
             [1,2,3,4],
             [7,8,9,10],
             [13,14,15,62]
    ])

m=matrix(arr4)
print(m)
#creating the above code is to much big lets do in short lines
from numpy import *

m=matrix('1 2; 3 4;5 6;7 8')
n=matrix('3 4 5;7 8 6;4 3 2')#so from here you want to print the diogonal part then use the diogonal function
print(m)
print(diagonal(n))
print(m.min())
print(m.max())
print(n.min())
print(n.max())



#write a code to multiply the two matrices using the 2d arrays and for loop
from numpy import *
m1=matrix('1 2 3;4 5 6;7 8 9')
m2=matrix('2,3,4;5 6 9;9 5 3')
m3=m1+m2
m4=m1*m2
print(m3)
print(m4)
