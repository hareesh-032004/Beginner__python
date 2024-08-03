#Socket Programming Using Python::..

#server side::

import socket
s=socket.socket()

print('socket created')

s.bind(('localhost',5555)) #port number starts from 0 to 65535

s.listen(3)

print('waiting for the connections')

while True:
   c,addr= s.accept()
   name = c.recv(1024).decode()
   print('connected with',addr,name)

   c.send(bytes('welcome to the Pycham','utf-8')) #here you have to senf it in the bytes format and you hav to mention the  which format you have to send it

   c.close()



#client's side::

import socket

c=socket.socket()

c.connect(('localhost',5555))

name=input('Enter your Name:')
c.send(bytes(name,'utf-8'))

print(c.recv(1024).decode()) #1024 is buffer size and that decode is used to no print the bytes in output:


#it will not run here see this in pycham for more clarification
   
