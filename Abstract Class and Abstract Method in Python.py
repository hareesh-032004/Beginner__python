#Abstract Class and Abstract Method in Python::...

#ABC-Abstract Base classes
from abc import ABC, abstractmethod
class computer(ABC): #Now this is abstract class
    @abstractmethod
    def process(self):
        pass #if you tell pass it simply means i don't have  anything inside this method now this methods which only has a declaration but not definition we call them as Abstract Method and the class which have the abstract methods is called as  the abstract classes

class Laptop(computer):
    def process(self):
        print('Running')

class Desktop(computer):
    def process(self):
        print('its is super')


class programmer():
    def work(self):
        print('sloving bugs')
        

#one more thing about abstract class is you cannot create a object of it Example:if we try to create a object of computer then it not show any error

#com1=computer() #This object is not an abstract class yet how do we make it ? By importing abc  
lap=Laptop()
lap.process()

desk=Desktop()
desk.process()

prog=programmer()
prog.work()




    
