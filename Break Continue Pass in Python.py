#Break Continue Pass in Python::

x=int(input("Enter the how many candy's you want?:"))

i=1
while i<=x:
    print("candy")
    i=i+1

#so here if candys are there it will give you candys but user asks for 100 candys but machine have only 50 candys then system want to tell "we don't have stock right now" so that we can use the break statement..

av=5
x=int(input("Enter the candy's:"))
i=1
while i<=x:
    if i>av:
        print("Out of stock")
        break
    
    print("candys")
    i=i+1
    
print("Exit")
#so here in above one the output is if you entered the number above 5 then it will not have that much cand's so that it will give 5 then it will tell that out of stock:


#without using continue printing the all the numbers without divisible by 3 upto 100::
for i in range(1,101):
    if i%3!=0:
     print(i)
    i=i+1


#with continue we can do like this:
for i in range(1,101):
    if i%3==0 or i%5==0: # here if you dont want the the numbers divisible by 5 then keep or and do 
        continue #here continue will skip the remaining stuff or fruther execution  so it will jump out of the loop it will only skip the remaining statements
    print(i)




#without using the pass print all the numbers 1 to 100 but don't print odd numbers:
for i in range(1,101):
    if i%2==0:
     print(i)
    i=i+1


#with pass,, pass simply means a there is no code ignore it::
for i in range(1,101):
    if i%2!=0:
        pass
    else:
        print(i)
    
    
