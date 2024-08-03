##42 Python Tutorial for Beginners | Anonymous Functions | Lambda:

def sqrt(a):
    return a*a
result=sqrt(5)
print(result)


#functions are objects in python and instead of creating a function we can use the lamda function to get lesser number of lines:

f=lambda a:a*a #anonymous function or lambda function
result=f(5)
print(result)




#lambda filter map reduce::
#so here we use three functions filter(),map(),reduce()
def is_even(n):
    return n%2==0
nums=[3,2,6,9,34,27,70,88,85]
evens=list(filter(is_even,nums))
print(evens)

#filter():
#if we use the lamda function in above case then we dont want to create a function
nums=[3,5,8,2,7,5,6,44,7,888]
even=list(filter(lambda n:n%2==0,nums)) #that's the beauty of using the lambda function
print(even)


#map():
from functools import reduce
nums=[3,5,8,2,7,5,6,4,7,9]
even=list(filter(lambda n:n%2==0,nums))
doubles=list(map(lambda n:n*2,even))
print(doubles)
#reduce():
sum=reduce(lambda a,b: a+b,doubles) # here we can't use the reduce directly we want to import it
print(sum)
