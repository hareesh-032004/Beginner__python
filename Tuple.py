Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
tup=(21,36,14,25)
tup
(21, 36, 14, 25)
tup[1]
36
# when you want to fetch values we can you sq bractets []

tup[1]=33
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tup[1]=33
TypeError: 'tuple' object does not support item assignment
# here we cannot change the value because tuple is a immutable

# here we can use certain methods like count and index
# here count ,menas it will count the number of occurrence of a number

tup.count()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    tup.count()
TypeError: tuple.count() takes exactly one argument (0 given)
tup.count(36)
1
tupl=(22,33,33,3,6,7,66)
tup.count(33)
0
tup1.count(33)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tup1.count(33)
NameError: name 'tup1' is not defined. Did you mean: 'tup'?


#set::
s={22,25,14,21,5}
# set never follows a sequence
s
{5, 21, 22, 25, 14}
s
{5, 21, 22, 25, 14}
s
{5, 21, 22, 25, 14}
s={22,14,98,63,90}
s
{98, 22, 90, 14, 63}
s
{98, 22, 90, 14, 63}
s={22,77,77,77}
s
{77, 22}
# so here 77 was printed only once because set uses a concept of hash and using hash we can improve our performance

s[2]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    s[2]
TypeError: 'set' object is not subscriptable
# in set index value is not supported ,because we don't have a proper sequence right it's not make any sence while you keeep index

s.add(45,72)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s.add(45,72)
TypeError: set.add() takes exactly one argument (2 given)
s.add(55)
s
{77, 22, 55}
s.add(33)
s
{33, 77, 22, 55}
# here we have so many in-built functions line add,clear,copy,difference,discard ,intersection,disjoint,pop,remove,union etc we have

nums=[25,36,95,14,12,26]
del nums[95,14,12]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    del nums[95,14,12]
TypeError: list indices must be integers or slices, not tuple
>>> nums.remove(2)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    nums.remove(2)
ValueError: list.remove(x): x not in list
>>> nums.remove[2]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    nums.remove[2]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> nums.remove(95)
>>> nums.remove(14)
>>> nums.remove(12)
>>> nums
[25, 36, 26]
>>> del nums[3:]
>>> nums
[25, 36, 26]
>>> del nums[1:]
>>> nums
[25]
>>> for nums in range(95,14,12)
SyntaxError: expected ':'
>>> for nums in range(95,14,12):
...     nums
... nums
SyntaxError: invalid syntax
>>> for value in range[95,14,12]
SyntaxError: expected ':'
>>> for nums in range[95,14,12]:
...    nums.remove(value)
... print(nums)
SyntaxError: invalid syntax
>>>   print(nums)
...   
SyntaxError: unexpected indent
