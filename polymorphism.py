x=5 #if you tell x=5 in your memory you have got a sapce which is of type int

x='Naresh' #if you tell 'Naresh'in your memory you have got a sapce which is of type str
#so here x is Just name to it

class pycham:

    def execute(self):
        print('compiling')
        print('Running')

class MyEditor:
    def execute(self):
        print('spell check')
        print('convenction check')
        print('compiling')
        print('Running')
        
        
class Laptop:
    def code(self,ide):
        ide.execute()
        
ide=MyEditor() #it does not matter which class object you are passing what matter is that object should have the execute method
#if there is a bird and if that bird behaves like a duck,it walks like a duck,and quacks like a duck,swims like a duck and it should be a duck in the same way if there is an object which is IDE and it has a method execute that it's we are not concerned about which class object it is waht we are concerned about it ,it should have that method which is execute and that is called as the duck typing

lap1=Laptop()
lap1.code(ide)
        
