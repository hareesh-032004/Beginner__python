#Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
#Import Math Functions in Python
#x=sqrt(25)
#Traceback (m,ost recent call last):
 # File "<pyshell#1>", line 1, in <module>

#NameError: name 'sqrt' is not defined
# so here we got an error so in python we have lot of modules to work with so these modules are by default not there for you so need to ask them by the help of 'import'

import math   # so here math is module in which you have all these functions
x=math.sqrt(25)
print(x)
5.0
x=math.sqrt(16)
print(x)
4.0
x=math.sqrt(15)
print(x)
3.872983346207417

#And here we have so many functions they are floor and ceil functions
#if we are using floor you need to go down ex: even it is 2.9 it will 2 if you use floor function
#if we are using ceil you need to go up ex:even it is 2.1 it will be 3 if you are using the ceil function lets try it once

print(math.floor(2.9))
2
print(math.ceil(2.9))
3
print(math.ceil(2.1))
3

#if you want to print the power function then you can do it
3**8
6561
print(math.pow(3,8))
6561.0


#we can get the pi value
print(math.pi)
3.141592653589793

#we can get the exponential value
print(math.e)
2.718281828459045


#so in every problem we cant use the math write there are so many modules so that we can use it as 'import math as m'
import math as m
math.sqrt(49)
7.0
m.sqrt(49)
7.0
#its working yaa hooooooooooooooooooo so if you are lazy to type then you can use this import math as m so here we use a concept called 'allies'

#so you dont want to use all the modules you want to import some modules only then you write like this ''from math import sqrt,pow'' here we are importing only two modules 'sqrt' and 'pow'


from math import sqrt,pow
pow(4,5)
1024.0
sqrt(100)
10.0
# here you dont want to call repetadlly modules because you are imported what you want
bin(7)
'0b111'
0b11100
28
125|265
381
652^125
753
(288<<2)>>(26//6)
72

import math
print(math.log(50,10))
