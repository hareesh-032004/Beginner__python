#64 Python Tutorial for Beginners | MultiThreading::..
#why do we need threads nowfirst of all what is a thread now basically if you can imagine an application let's say if you have MS word that one application will have certain subclasses right so in ms word we can type appointment we can change the font of it you know we can save that in  some other formats so MS Office provide you so many features so

#we can break down one task into multipleprocess and then again we can break down those process into a trader so you can imagine thread as a lightweight processor when you break down the bigtask into small parts each part will be called thread

from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(1)#if we don't use the sleep then our cpu is fast so that we get same time our output so will be a collsion so in cpu there is a concept called as schedulers which will give you a specific time to execute 



class Hi(Thread):
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(1)

#By default every execution has one thread s even you are not getting thread by your self you do have one thread called as Main Thread

t1=Hello()
t2=Hi()

t1.start() # if you want to create a two different methods then instead of calling the run method call the start method so when you say t1.start behind the scence run method is called so run is a in-built method to use 
sleep(0.2)
t2.start()#when you say start it creates a two different threads

t1.join()# after satraing the t1 and t2 t1 is printing hello and t2 is printing hi and main is doing nothing write so main says my job is to print Bye we don't want that so we want to ask the main thread wait for t1 and t2 to join so you use t1.join() and t2.join() 
t2.join()

#collision happens when two threads are coming at the same time to the cpu

print('Bye')
        
        
