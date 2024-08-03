#54 Python Tutorial for Beginners | Inner class::..
class student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        self.lap=self.Laptop()

    def show(self):
        print(self.name,self.roll_no)
        self.lap.show()

    
    class Laptop:

        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram=8

        def show(self):
            print(self.brand,self.cpu,self.ram)

       
           
s1=student('Naresh',13)
s2=student('Nani',46)

s1.show()
s2.show()

#you can create object of inner class inside the outer class
#or you can create object of inner class outside the outer class provided you use outer class name to call it

lap1=s1.lap
lap2=s2.lap
print(id(lap1))
print(id(lap2))




#Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
from datetime import datetime
class person:
    def __init__(self,name,country,d_o_b):
        self.name=name
        self.country=country
        self.d_o_b=datetime.strptime(d_o_b,"%d-%m-%Y")


    def cal_age(self):
        today=datetime.today()
        age=today.year-self.d_o_b.year

        if today.month<self.d_o_b.month or (today.month==self.d_o_b.month and today.day<self.d_o_b.day):
            age=age-1

        return age

name=input('Enter the persons name:')
country=input("Enter the person's country:")
d_o_b=input("Enter the person's date of birth (DD-MM-YYYY):")

person=person(name,country,d_o_b)
age=person.cal_age()

print(person)
print('The age of the person is:',age)
        
