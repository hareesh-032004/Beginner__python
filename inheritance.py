#55 Python Tutorial for Beginners | Inheritance:...
#A->B IS CALLED AS SINGLE INHERITANCE:::....
#A->B->C IS CALLED AS THE MULTI LEVEL INHERITANCE:...
#A<-C->B is calles as the Multipel inheritance menas ascessing the both classes at time

class A: #This is called as super class or parent class
    def feature1(self):
        print('Feature 1 working')

    def feature2(self):
        print('Feature 2 working')    


class B(A):#This b is an child class or sub-class if we keep class B(A) like this so this is inheriting the features of the class A
    
    def feature3(self):
        print('Feature 3 working')

    def feature4(self):
        print('Feature 4 working')



class C(B):#so here c we an acess the features of class A and class B ,if we keep like this class C(A,B): it is accesing the features of A directly so it called as the multiple inheritance::...
    def feature5(self):
        print('Feature 5 working')
     
#creation of objects of A
a1=A()
a2=A()

#creation of objects of B
b3=B()
b4=B()

#creation of objects of C
c5=C()


a1.feature1()
a2.feature2()

b3.feature3()
b4.feature4()

c5.feature5()

