# Array values from User in Python
from array import *
arr=array('i',[]) #Empty array
n=int(input("Enter the length of the array:"))
for i in range(n):
    x=int(input("Enter the next value:"))
    arr.append(x)

print(arr)

#if you want to print the index number also from the given array then:
val=int(input("ENTER THE VALUE FOR SERACH:"))
k=0
for e in arr:
    if e==val:
        print(k)
        break
    k=k+1
#so we can write with function also but in that we don't want to write the loop here.. ,just use the index function..
print(arr.index(val))    



#1) Create an array with 5 values & delete the value at index no. 2 without using in-built function. 
#2) write a code to reverse an array without using in-built function.

#without in built function:
from array import *
arr=array('i',[])
for i in range(5):
    n=int(input("Enter the next value:"))
    arr.append(n)
print('Array before delection:',arr)

for i in range(2,len(arr)-1):
    arr[i]=arr[i+1]
arr.pop()
print('Array after delection:',arr)


#with inbuilt:
from array import *
arr=array('i',[])
for i in range(5):
    n=int(input('Enter the next values:'))
    arr.append(n)
print("Array before delection is",arr)

arr.pop(2)
print("Array after delection is:",arr)

    
#2) write a code to reverse an array without using in-built function.
#without inbuilt:

from array import *
arr = array('i', [])
for i in range(4):
    n = int(input("Enter the values: "))
    arr.append(n)
reversed_arr = array('i', [])
for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])
    
print('The reverse order of the array is:', reversed_arr)

#with inbuilt:
from array import *
arr=array('i',[])
for i in range(4):
    n=int(input("Enter the values:"))
    arr.append(n)
arr.reverse()
print('The reverse order of the array is:',arr)

