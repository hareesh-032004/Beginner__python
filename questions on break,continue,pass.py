#1.)print first 50 fibonacci numbers.

a=0
b=1
count=0

while True:
    print(a)
    count=count+1
    if count==50:
        break
    if a<0:
        pass
    a,b=b,a+b
    if a>1000:
        continue


#2.)check a given number is prime or not
num=int(input("Enter the number:"))
if num<=1:
    print("It is not a prime number")
else:    
    for i in range(2,int(num**0.5)+1):
       if num%i==0:
          print("Its is Not a prime number")
          break
    else:
       print('Its is a prime number')



#continue question:
for i in range(5):
    if i==3:
        continue #if you don't want the third iteraion then use the continue
    print("Naresh",i)

#so what break will do is it will stop if that condition is done
for i in range(5):
    if i==3:
        break
    print("Naresh",i) # here we gave the range 5,but we breaked it in 3rd itrertion so tha only 0,1,2 got printed



#so we use pass for thing those function is empty you know you want it but not now in use the we use that ex:
#def fun():
 #   print('statements')
  #  print("statemnts")
 #a=5 # here we have some data what if i dont want now i will do it use by later then we use pass:


#def fun():
 # pass
 #a=5  

  
