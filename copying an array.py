#Copying an Array in Python
from numpy import *
arr=array([1,2,3,4,5,6])
arr1=array([7,8,9,10,11,12])
arr2=array([13,14,15,16,17,18])
arr=arr+5
arr3=arr1+arr2
print(arr)
print(arr3)


#and here we can find the trignometric values also
arrr=([1,23,10,80,70,260])
print(sin(arrr))
print(cos(arrr))
print(log(arrr))
print(sqrt(arrr))
print(sum(arrr))
print(min(arrr))
print(max(arrr))
print(sorted(arrr))
print(unique(arrr))
print(concatenate([arr,arrr]))


from numpy import *
arrr=array([7,8,9,10,11,12])
arr=arr1
print(arrr)
print(arrr)
print(id(arrr))
print(id(arrr)) #here id of the arr and arr1 has the same address because of the Aliasing concept 

#how to change the different address , by using the function called view()
arrr=array([7,8,9,10,11,12])
arr=arr1.view() #here we have an different address but same array because we are copying it write.. 
print(arrr)
print(arr)
print(id(arrr))
print(id(arr))


#we we have two types of copying they are:shallow copy and deep copy..
#shallow copy means:it will copy the elements but both the array still dependent on each other

a1=array([7,8,9,10,11,12])
a2=a1.view()
a1[3]=25
print(a1)
print(a2)
print(id(a1))
print(id(a2))


#deep copy:They are two different arrays and they are not linked with each other

a1=array([7,8,9,10,11,12])
a2=a1.copy() #here we are giving the different values and two different arrays not linking with other that's intresting write
a1[3]=25
print(a1)
print(a2)
print(id(a1))
print(id(a2))



#write a code to add 2 arrays using the for loop:
#without using the inbuilt functions
from array import *
arr1=array('i',[])
arr2=array('i',[])
print('Enter the values of the first array:')
for i in range(4):
    n=int(input("Enter a value:"))
    arr1.append(n)
    

print('Enter the values of the second array')
for i in range(4):
    n=int(input("Enter a value:"))
    arr2.append(n)
result_arr=array('i',[])
for i in range(len(arr1)):
    result_arr.append(arr1[i]+arr2[i])
print("The array after addition is:",result_arr)


#with-inbuilt functions
from array import *
arry4=([54,36,54,65,68,98])
arry5=([65,69,74,34,90,67])
arr6=array('i',[])
for i in range(len(arry4)):
    arr6.append(arry4[i]+arry5[i])
print('The array after the addition is:',arr6)    
          



