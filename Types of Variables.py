#52 Python Tutorial for Beginners | Types of Variables
#here we have two types of variables they are Instance variable,class(static)variable

class car:
    wheels=4
    def __init__(self):
        self.mil=10
        self.com='BMW'#this two are instance varibles mil and com
#object creation
c1=car()
c2=car()
c1.mil=20
car.wheels=10
print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)
        



#if you define the variable inside init it becomes an instance variable, if you define a variable outside init then it becomes a class variable
#namespace is an area where you create and store object/variable
                  #1.class namesapce
                  #2.object/instance namesace


