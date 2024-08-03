#for else in python
nums=[12,15,20,33,65]
for i in nums:
    if i%5==0:
        print(i)# if you want to print only the first divisible number then use break:
        

#use of break will print only first divisible number
nums=[12,15,20,33,65]
for i in nums:
    if i%5==0:
        print(i)
        break


#what if if you don't have a number in the list
nums=[1,12,14,16,18]
for i in nums:
    if i%5==0:
        print(i)
        break
    else:
        print("Not found")

# if you write here the output will be printed 5 times,because it's chekingfor the each iteration of tha case so we don't want that so keep the else case for the for loop not for the if block::
nums=[1,12,14,16,18,22]
for i in nums:
    if i%5==0:
        print(i)
        break # here break is very important..
else: # change this iteration then it will print only once
    print("Not found")
