#60 Python Tutorial for Beginners | Method Overloading and Method Overriding:...

#Method overloading:If you have a class and in that class if you have let's say two methods with the same name but different parameters or arguments which is called as method overloading

#Example:
#class student:
    #method is def average(a,b)
    #method is def average(a,b,c) #same name but different parameters



#Method Overriding:If you have two methods with the same name and same number of parameters or arguments but not in the same class but let's say the concept of inheritance we have class A and class B and both the class have the same method with the same name same parameter this is called as the method overriding


#method overloading ex:

class  student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    

    #adding two numbers
    def sum(self,a=None,b=None,c=None): #we can create a method inside a class which takes two parameters and pass two parameters it works what if we want to pass the three values
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None: #so by  using this we can have how many arguments we want if we not pass also we get not an error because it's takes the none value
            s=a+b
        else:
            s=a
            
        return s
    

s1=student(58,90)
print(s1.sum(32,45,89))#if we pass the three argumets we got an error because we are acceting only two values if we keep in above (a,b,c) then it is correct
#if we have (a,b,c) in above but we pass two arguments then also we will get an error
#to solve that we have to keep a=None,b=None,c=None





#Method over riding:

class A:
    def show(self):
        print('In A show')


class B(A):# here we are inherting the super class A
     def show(self):
        print('In B show')#so B class lo kani show method kani untey apudu B class lo unna method print iyidhi leka pothe inherit cheskunamm kabati Class A lo unna show  method print iyidhi:..
     pass #AttributeError: 'B' object has no attribute 'show' at this stage we use a concept called inheritance

#***** when you call show it will call this show method of this sub-class if-you have it okayy.....

s1=B()
s1.show() #output- print('In A show')#if we not define the show method in B then it will go to Class A

s2=A()
s2.show()
