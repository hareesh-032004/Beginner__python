Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# so data types we have here is None,Numeric,List,Tuple,Set,String,Range,Dictionary or Map

#1.)None: when you have a variable and if that variable is not assigned with any value then it is none in other languages it is called as Null

#2.)Numeric:In nuemric we have 4 types they are int,float,complex,bool lets see that with an example

num=5
type(num)
<class 'int'>

num=10.55
type(num)
<class 'float'>

num=5+10j
type(num)
<class 'complex'>

num=True
type(num)
<class 'bool'>

# can we convert from one data type to another?? yes
a=25.55
b=int(a)
b
25

k=float(b)
k
25.0

# can we convert a normal number in to a complex number?? yes
k=50
c=complex(b,k)
c
(25+50j)

b<k
True
corr=b<k
type(corr)
<class 'bool'>
b>k
False

# we know that true menas 1 and false means 0
int(True)
1
int(False)
0


# when we say this list,Tuple,set,string,Range all will comes under Sequence

lst=[23,44,2,23,55,7,88]
type(lst)
<class 'list'>

Tup=(25,66,22,74,3,5,11,55)
type(Tup)
<class 'tuple'>

s={2345,123456,123,1234,}
s
{123456, 2345, 1234, 123}
type(s)
<class 'set'>

str='Naresh'
type(str)
<class 'str'>
# here char is also nothing but string
ch='N'
type(ch)
<class 'str'>


#when we iterate between values we can use range like

range(100)
range(0, 100)
list(range(100))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]


# if you want to do range with different iterations like  different difference

>>> list(range(2,100,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> 
>>> type(range(100))
<class 'range'>
>>> 
>>> 
>>> d={'Naresh':'Iqoo','Hareesh':'One-plus','Akhil':'Iphone'}
>>> d
{'Naresh': 'Iqoo', 'Hareesh': 'One-plus', 'Akhil': 'Iphone'}
>>> 
>>> # how we know naresh,hareesh,and akhil is keys lets do it
>>> d.keys()
dict_keys(['Naresh', 'Hareesh', 'Akhil'])
>>> dict_keys(['Naresh', 'Hareesh', 'Akhil'])
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    dict_keys(['Naresh', 'Hareesh', 'Akhil'])
NameError: name 'dict_keys' is not defined
>>> # and if want the values they do like this
>>> d.values()
dict_values(['Iqoo', 'One-plus', 'Iphone'])
>>> 
>>> # how we can get a particular value in lists we have index value but in this we have onlu key values write .......
>>> d['Akhil']
'Iphone'
>>> d['Naresh']
'Iqoo'
>>> # instead of sq [] we can use () brackets by using the get function
>>> d.get('Akhil')
'Iphone'
>>> d.get('Hareesh')
'One-plus'
>>> 'One-plus'
'One-plus'
>>> d.get('Naresh')
'Iqoo'
