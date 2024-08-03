Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

num=5
# if you want to get the address of the variable name you will use the function called   id()
id(num)
140720105716280
name='Naresh'
id(name)
2149045751360

a=10
b=a
\
a
10
b
10
# here we got the same value that is 10
id(a)
140720105716440
id(b)
140720105716440
# so here we got the same addresses so in python what happens is whenever you create multiple variables and in case if they have the same data then they both will point to the same box they will not get the multiple boxes for each variable thats where python is more memory efficient right because you are not getting the multiple data here that's great
id(10)
140720105716440

# here in future if we want to change the variable suppose you keeep 'k'
k=10
id(k)
140720105716440
# here also you got the same address so it is not focusiing on the variable system is giving its focuing on the partikular value like 10 so here 10 is a value and your tagging 'a','b','k' in the same object


# what happens if we change the value of a 'a' it will effect the address of the 'a'??
a=20
id(a)
140720105716760
id(b)
140720105716440
## here b is assingned to the same addreess we menctioned before b=a
# if we keep k=a then see
k=a
id(k)
140720105716760
id(b)
140720105716440

>>> # if in future we have an another value then
>>> b=8
>>> id(b)
140720105716376
>>> # so here we have a,b,k so a,k is refereing to the value 20 and b is refering to the value 8 so what happens to tha value 10 is there in the moemory  but no one using it, in python its is called as the garbage collection
>>> 
>>> PI=3.14
>>> PI
3.14
>>> PI=3.19
>>> PI
3.19
>>> #we know that pi is constant but in python you cannot make it constant but you can show your intenctions
>>> 
>>> # we can know the which type it is
>>> type(PI)
<class 'float'>
>>> name='Naresh'
>>> type(name)
<class 'str'>
>>> # like str,int,float, etc we have some in-built data types see that in next video.....
>>> num=10
>>> type(num)
<class 'int'>
>>> a=true
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> a=True
>>> type(a)
<class 'bool'>
>>> b=False
>>> type(b)
<class 'bool'>
