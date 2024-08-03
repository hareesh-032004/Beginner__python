#for loop in python, for loop is bacically working on the sequence not on the iteration if we see in while loop we want to keep the iteration incerment or decrement

x=['naresh',98,9.887]
print(x)
#if you print you will get it, but what if you want output by separatelyy or individually
# so syntax here is
for i in x:
    print(i)

#so you want to print a string separetely then
y='Naresh varma'
for i in y:
    print(i)



#so it can be anything you can write string,list,tuple,set here
for i in ['Naresh',16-5-2005,19]:
    print(i)


for i in 'Naresh':
    print(i)

#here also we can print numbers in certain range in for loop
for i in range(2,101,2):
    print(i)

for j in range(2,10):
    print(j)

#so if you want to do in reverse order you have to menction it in -ve

for k in range(100,1,-5):
    print(k)




#so in 100 numbers 3 and 5 numbers are not divisible
for z in range(1,101):
    if z%3!=0 and z%5!=0:
     print(z)



#print all the perfect square numbers between 1 and 500.

#code:
import math     
for p in range(1,501):
    sqrt=math.isqrt(p)
    if sqrt*sqrt==p:
        print(p)

#another method is
# Iterate through possible square roots
for i in range(1, int(500**0.5) + 1):
    perfect_square = i * i
    print(perfect_square)
        
        

    
 
     
    

    
