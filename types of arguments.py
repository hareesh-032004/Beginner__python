#Types of Arguments in Python::
def add(a,b): #here a,b is called as the formal arguments
    c=a+b
    print(c)

add(5,6)#here 5,6 is called as the actual arguments

#here in actual itself we have 4 types :position,keyword,Default,Variable length

#position:
def person(name,age):
    print(name)
    print(age)
person('Naresh',19)#here name knows the postion of the string and age knows the value of integer

#if we change the arguments passing into it then:
def person(name,age):
    print(name)
    print(age)#print(age-5) then we got an error becasue string cant do subcatrion write its not make any sence....
person(19,'Naresh')# if we do it like that it comes but if we do some opertions then we get an error 

#if we assign like this its okkk..
def person(name,age):
    print(name)
    print(age)
person(age=19,name='Naresh') #so in this case we used the keywords


#Default is used as if we ant to open an account then cireteia should be above 18 write so by default its is 18 if you are enterting it above 18 ,it will override the value lets see that
def person(name,age=18):
    print(name)
    print(age)
person(name='Naresh',age=19) #if you not give the 19 then by default it will give the 18



#variable length argument():means in above case we are taking only the two varibles write but what if we want more numbers to do
def add(a,*b):#here *b means we dont know the values how much you want
    c=a
    for i in b:
        c=c+i
    print(c)

add(5,10,20,30,40,50)#here 5 assins to a remaing numbers assing to be b as *b    


#so here we can write a code without using the a value also
def nani(*b):
    c=0
    for i in b:
        c=c+i
    print(c)
nani(5,6,7,8,91,2,3,5,6)    
    


