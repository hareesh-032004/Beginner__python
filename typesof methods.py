#53 Python Tutorial for Beginners | Types of Methods::..

#here we have three(3) types of methods 1.)Instance methods 2.)class methods 3.)static methods but in varibles class and static are same but here it's different
#in instance itself we have 2 types: Accessor methods-> is used to fecth the valuses means (get) and Mutator methods-> is used to modify means(set)the valuses


class student:
    college='Amrita'
    
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self): #self belongs to an partikular object.
        return (self.m1+self.m2+self.m3)/3
    
    @classmethod #this is called as deocorators
    def info(cls):
        return cls.college

    def get_college(cls):
        return cls.college
    
    @staticmethod
    def info1():
        print('this is student class')
    
    
        

    #def get_m1(self):
     #   return self.m1
    
    #def set_m1(self,value):
     #   return self.m1




mat=student(50,79,77)
phy=student(88,40,46)
che=student(50,100,78)

print(mat.m1,mat.m2,mat.m3)
print(phy.m1,phy.m2,phy.m3)
print(che.m1,che.m2,che.m3)

print(mat.avg())
print(phy.avg())
print(che.avg())

print(student.info())
print(student.info1())
