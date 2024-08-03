#59 Python Tutorial for Beginners | Operator Overloading | Polymorphism::..
#5+6 here 5 and 6 are operands and + is a operator we can add int and float numbers what about strings can we add them lets's see that:..

a=5
b=6 #if we keep 'string here' we get an type error 
print(a+b)#TypeError: unsupported operand type(s) for +: 'int' and 'str'


a=5
b=9
print(a+b)# here if we called print(a+b) behind the secence this only will occur print(int.__add__(a,b))
#or you can say
print(int.__add__(a,b))# we have so many methods like __init__(self,x),__abs__(self),__add__(self,x) and we have so many methods


#here we can add two strings so that it concatinates(combined)
a='Naresh '
b='Hasthi' #The moment you changed the type of it it will not work because the in-built class does not have two things which is integer and string together

print(a+b)
print(str.__add__(a,b))



class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other): #we have cerated our own add method
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        
        return s3
        
    def __gt__(self,other): #we have created our own greater than method:.
        r1=self.m1+other.m2
        r2=self.m1+other.m2
        if r1>r2:
            return True
        else:
            return False
        

    def __str__(self):
        return '{} {} '.format(self.m1,self.m2)
    
s1=student(58,69)
s2=student(60,100)



s3=s1+s2 #TypeError: unsupported operand type(s) for +: 'student' and 'student'
#we say s1+s2 waht it want to do compiler don't know what to do so we want to define a function add.

if s1>s2:
    print('s1 wins:')

else:
    print('s2 wins:')

    
print(s3.m2)





#here if
a=9
print(a)# behind the sence this is happening  (a.__str__())
print(a.__str__())


print(s1) #if we run this we got the address <__main__.student object at 0x000002B1730BC5C0> of the s1 we don't want that we want values then create the method str 
#or we can do write this as
print(s1.__str__())
print(s2)


#when  you perfrom any operator like addition,sub,mult,division,gt,ge,lt,le behind the scene we are calling the methods like __add__(self,other) like that only remaining





#Example:

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)



cat1.info()
cat1.make_sound()
dog1.info()
dog1.make_sound()
