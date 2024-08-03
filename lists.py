Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

nums=[25,12,36,72,82]
nums
[25, 12, 36, 72, 82]

nums[0]
25
#before also we worked like this only index
nums[3]
72
nums[2:]
[36, 72, 82]
# here you have given the index 2 and soo onn thats why upto end its printed
nums[-1]
82
nums[-3]
36
#same here also
#25,12,36,72,82
#0 ,1 ,2 ,3, 4
#-5,-4,-3,-2,-1
nums[-5]
25

names=['Naresh','Navadeep','Nani']
names
['Naresh', 'Navadeep', 'Nani']

#we can have a list with different type of data like integer,float,string thats the beauty of the lists
values=[9.5,'Naresh',20]
values
[9.5, 'Naresh', 20]
mil=[nums,names]
mil
[[25, 12, 36, 72, 82], ['Naresh', 'Navadeep', 'Nani']]
mil=[nums,names,values]
mil
[[25, 12, 36, 72, 82], ['Naresh', 'Navadeep', 'Nani'], [9.5, 'Naresh', 20]]
#amazing thing about lists is we can perform certain operations becasue it has certain methods or we can call as functions

#another thing about list list is it is mutable menas we can simply change the values
nums.append(45)
nums
[25, 12, 36, 72, 82, 45]
# here append means 45 is added at the end of the value
nums.insert(90)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    nums.insert(90)
TypeError: insert expected 2 arguments, got 1
# here we got the error because we should menction the index value where we want to insert the value in between
nums.insert(3,90)
nums
[25, 12, 36, 90, 72, 82, 45]

#we can delete by giving remove()
nums.remove(82)
nums
[25, 12, 36, 90, 72, 45]


#here if we pop() then we can delete through index number
nums.pop(1)
12
nums
[25, 36, 90, 72, 45]

nums.pop()
45
nums
[25, 36, 90, 72]
# here 45 is removed if we dont menction the index value it will pop out th lastly added number so from nums 45 is lastly added

# if you want to delete a multiple values the use this
del nums[2:]
nums
[25, 36]
# so here from index the values got deleted

# here we can extend the values
nums.extend(30,45,88,21,32)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    nums.extend(30,45,88,21,32)
TypeError: list.extend() takes exactly one argument (5 given)

>>> # so here you should keep the [()] like this
>>> # so here you should keep like this ([]) not like above line
>>> nums.extend([30,45,88,21,32])
>>> nums
[25, 36, 30, 45, 88, 21, 32]
>>> 
>>> # in python we have in-built functions like max,min,len,etc
>>> max(nums)
88
>>> 
>>> min(nums)
21
>>> sum
<built-in function sum>
>>> sum(nums)
277
>>> 
>>> l_n=['Naresh','Nani']
>>> len(l_n)
2
>>> list=['Naresh hasthi varma']
>>> len(list)
1
>>> list=['Nareshhasthivarma']
... len(list)
SyntaxError: multiple statements found while compiling a single statement
>>> listi=['Naresh hasthi']
... len(listi)
SyntaxError: multiple statements found while compiling a single statement
>>> nums.sort()
>>> nums
[21, 25, 30, 32, 36, 45, 88]
>>> # so here lists is amazing its provides the soreted format
>>> 
>>> 
>>> # output tell mee
>>> name="Telusko"
>>> print(name[-3])
s
>>> name[-3]
's'
