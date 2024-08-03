##37 Python Tutorial for Beginners | Pass List to a Function in Python::


def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
    return even,odd

lst=[20,25,14,19,16,24,28,47,26]
even,odd=count(lst)
print('Even numbers are:',even)
print('odd numbers are:',odd)



#write a code for taking 10 names from the user and which has more than 5 letters 
def count_long_names(lst):
    more_than_5 = 0
    less_or_equal_5 = 0
    for name in lst:
        if len(name) > 5:
            more_than_5 += 1
        else:
            less_or_equal_5 += 1
    return more_than_5, less_or_equal_5

# Initialize an empty list to store the names
names = []

# Loop to take 10 names as input from the user
for i in range(10):
    name = input("Enter name {}: ".format(i + 1))
    names.append(name)

# Get the count of names with more than 5 letters
more_than_5, less_or_equal_5 = count_long_names(names)

# Print the results
print('Names with more than 5 letters:', more_than_5)
print('Names with 5 or fewer letters:', less_or_equal_5)



# Fibonacci Sequence:0 1 1 2 3 5 8 13 21...
a=0
b=1
count=0
while True:
    print(a)
    count=count+1
    if count==50:
       break
    if a<0:
        pass
    
    a,b=b,a+b
    if a>1000:
        continue



#By using functions write a fibonacci seq code:

def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(15)



#assignment solution:
x = int(input("enter till how many numbers you want fibonacci series = "))


def fibo(n):
    a = 0
    b = 1
    if n < 0:
        print("invalid value enter a valid one!")
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):# 2 elements are printed so 0 and 1 are already occupied now from index 2 start
            c = a+b
            a = b
            b = c
            if c > 100:
                break
            print(c)


fibo(x)



#factorial in python:

x=int(input('enter the number:'))
fact=1
for i in range(1,x+1):
    fact=fact*i
print('The factorial of your number is:',fact)


#write a factorial using the functions in python:
def facto(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
y=int(input('Enter the value of your number:'))
result=facto(y)
print(result)
        






