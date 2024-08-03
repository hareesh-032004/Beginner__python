#56 Python Tutorial for Beginners | Constructor in Inheritance:..
#sub class can access all the features of super class but superclass can not access any features of sub class
#if you create a object of sub-class it will first try to find init of sub-class if it is not found then it will call init of super class
class A:
    def __init__(self):
        print('in A init')

    def feature1(self):
        print('Feature 1 working')
    def feature2(self):
        print('Feature 2 working')

class B: #you should keep class B(A): then B is a sub-class and A is a super-class
    def __init__(self): 
        super().__init__ ()  #when you say super you can acesses all the features of the parent class we don't want to call to seperately

#point is when you create object of sub-class it will call init of sub-class first, if you have call super then it will first call init of super class then call init of sub-class        
        print('in B init')
    
      
    def feature3(self):
        print('Feature 3 working')    

    def feature4(self):
        print('Feature 4 working')

class C(A,B):
    def __init__(self):
        super().__init__()
        print('in C init')

    def feat(self):
        super().feature2() #here we can call without using the init method by keeping the method name feature2() like that

        

#by default it will call B init what i want to acess the A also ,,then we use the super keyword
a2=C() #if we run this we got only a A and C but not B this is wrong, to talke that we have an concept of Method Resolution Order(MRO) This means it will take the left one first

a2.feature1()
a2.feat()

      
