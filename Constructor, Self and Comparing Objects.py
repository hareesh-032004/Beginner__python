#51 Python Tutorial for Beginners | Constructor, Self and Comparing Objects::.

class computer:
    def __init__(self):
        self.name='Naresh'
        self.age=19
    pass #we should not keep the class empty so use pass:

    def update(self):
        self.age=20


c1=computer()
c2=computer()


c1.name='Charan'
c2.name='srikanth'
c1.age=19
c2.age=18


c1.update()# here update have two objects c1,c2 which i want to call (we are not keeping any thing inside this brackets then how it know so that only we use self, so self is a pointer directing to c1 or c2 based on what you are calling)

print(c1.name)
print(c2.name)# so here we output is two times name() so it is automatically calls the object c2. so to change that befor printing you can change that
print(c1.age)
print(c2.age)



print(id(c1))#2785050938832 this is address of this c1 it is stored in some where in heap memory.
print(id(c2))#2512364948032 as we run this we any each time one one address because each time the object is created for you
#so imp is Every time you create an object it is allocated to new space::
#so size of that object is 1mb?,1kb?,5kb who knows who allocates size to object?? its is constructor
## so size of an object Depends upon the number of variables and size of each variable you have and





class computer:
    def __init__(self):
        self.name='Naresh'
        self.age=19

    def update(self):
        self.age=20


    def compare(self,c2):
        if self.age==c2.age:
            return True
        else:
            return False
c1=computer()
c1.age=35
c2=computer()


if c1.compare(c2):
    print('They are same:')
else:
    print('They are Different')

print(c1.name)
print(c2.age)




#Write a  Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math
class Circle:
    def __init__(self,r):
        self.r=r
        
    def cir_area(self):
        return math.pi*self.r**2
    def cir_peri(self):
        return 2*math.pi*self.r


r=float(input("Enter the value of the radius:"))
c=Circle(r)
a=c.cir_area()
p=c.cir_peri()

print('The value of the area is:',a)
print('The value of the perimeter is:',p)



list=[23,43,45,35,4,23,232,300,2,568,7,5]
print(max(list))




    











    
