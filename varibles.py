Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
2+3
5

x=2 #variable is a container where you can put your values or store values
x+5
7

y=3
x+y
5
x=9
x+y
12
#we can change the values also
x
9
abc
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    abc
NameError: name 'abc' is not defined. Did you mean: 'abs'? Or did you forget to import 'abc'?
x+10
19
19+y
22
#or we can use the _ symbol to represent the previous output
_+y
25
#22+3=25


name='Youtube'
name
'Youtube'
name+'rocks'
'Youtuberocks'
name 'rocks'
SyntaxError: invalid syntax
#we want keep compusorly + symbol then only string will concatenate
name[0] # if we want to fetch any letter in a string we use square brackets and here in youtube 0 index is 'y'
'Y'
name[6]
'e'
name[8]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    name[8]
IndexError: string index out of range
name[-1]
'e'
##Y O U T U B E
##0 1 2 3 4 5 6
#-7-6-5-4-3-2-1
#thats why when we print name[-1] we got 'e'
name[-7]
'Y'
name[-4]
't'


name[0:2]  #this 2 doses not means number of characters ,it means the ending
'Yo'

name[1:4]
'out'
# so here we cannot include index 4 we stop at index 3 only

name[1:]
'outube'
>>> ## here what happend means i started with index 1 and i dont have limitaions cointinue upto last index so ""outube"" came
>>> 
>>> name[:4]
'Yout'
>>> # here it will start at index 0 and end at index 3
>>> 
>>> name[3:10]
'tube'
>>> ## here it will start at index 3 and end at the last one which is available so
>>> 
>>> name[0:3]='my'
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    name[0:3]='my'
TypeError: 'str' object does not support item assignment
>>> 
>>> ##here it is saying that once you assin the value you cannot change it, that means strings in python is immutable
>>> 
>>> ##But we can do by keeping it before like
>>> 'my'+name[3:]
'mytube'
>>> myname="NARESH HASTHI"
>>> len(myname)
13
>>> ## len is inbuilt function to find the length of the string
>>> 
>>> myfrdname="Srikanth Reddy vanga"
>>> len(myfrdname)
20
>>> print(myfrdname)
Srikanth Reddy vanga
>>> 
>>> 
>>> print(r'Telusko\n Rocks')
Telusko\n Rocks
>>> 
>>> 
