#Keyworded Variable Length Arguments in Python | **kwargs:

def person(name,*data): #normalyy people will say only name write they don't tell the age,palce pho num etc so that'sy we aare accesing only the name
    print(name)
    print(data)
person('Naresh',19,'Naidupeta',6304836005) #the moment you run the code you see the output as the name and the tuple    

#so there is a concept called keyword variable length arguments if you pass the kayword let's see
def person1(name,*data):
    print(name)
    print(data)
person1('naresh',19,'Nellore',9272908202)# when you run this code others can't find out the what is naresh,nellore whetthre it is working palce or home place so instead of that confusion we use the keywors lets see that



def person2(name,**data):#keep another * to get the output correct
    print(name)
    print(data)
person2(name='Nani',age=19,place='Mumbai',mob_no=6304836005)
#so when you run this above code you will get an error because when you say *it will not accept the  keyword argument so that's y we use the ** there so that keyword argument will accept that 
def person3(name,**data):
    print(name)
    print(data)
person3(name='Navadeep',age=19, palce='Nellore',mob=6304836005)


#so with the help of for loop also we can do:
def p4(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
p4(name='Naresh',age=19,city='Chennai',ph_no=8930932988)        


