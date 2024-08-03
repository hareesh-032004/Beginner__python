#48 Python Tutorial for Beginners | Object Oriented Programming | Introduction
#object will have two things attributes->data and certain behaviour->actions
#so we have objects,classes, encapsulation,abstraction,polymorphism
#class is a design or you call call this as blue print and object is an instance


#I want to work with a computer then i need a blue print of that computer
#to define that we use class in that we can keep two things Attributes->Varibles and Behaviour->Methods(Function).

class computer:
    
    def config(self): #here self is the object you are passing
        print('i5,16gb,1TB')

a='10'
print(type(a))#output:<class 'str'> here str is a inbuilt class and down computer is a our own class

com1=computer()
print(type(com1)) #output:<class '__main__.computer'> #this is a class belongs to a computer and main is a module name

#how to call before we used to call is config() but in class and objects we should  call like this with class name and method name:computer.config()

computer.config(com1) #if we run this we got an error because one class have an multiple objects but in this case we ar using the only one object which is com1,the thing is config function or method will change behaviour based on the object write.. because different objects have different behaviour depend upon waht they know
#here we are calling config and passing com1

#and we can call this above as another like:
com1.config()

       
        
        
    
