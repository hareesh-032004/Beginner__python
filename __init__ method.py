#50 Python Tutorial for Beginners | __init__ method::

class computer:
    def __init__(self,cpu,ram): #init to intialse the variables
        self.cpu=cpu #if you want to be a part of the object, object means self so self.cpu,self.ram: 
        self.ram=ram
        print('in init')#we don't want to call it,it will be called automatically
        #if we run this code we get two times 'in init' because every object it calles onece, it has two objects so it calls 2 times..
    
    def config(self):
        print('config is:',self.cpu,self.ram)#print('config is',cpu,ram) if you print like this you will get an error because Cpu is not a local variable,its is belongs to an object so use self.cpu,self.ram:: 

com1=computer('i5',16)#in above you passed three(3) argumets they are self->means com1 or object  and i5->means cpu and 16-> means Ram 
com2=computer('Ryzen 3:',8)
com1.config()
com2.config()
