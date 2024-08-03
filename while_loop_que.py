#1.)write a code to print all the value from 1 to 100.skip the numbers which are divisible by 3 or 5.

num=1
while num<=100:
    if num%3!=0 and num%5!=0:
     print(num)
    num=num+1



#2.)write a code to print below pattern
    #####
    #####
    #####
    #####

#code:
i=1
while i<=4:
    print('#',end="")
    j=1
    while j<=4:
        print('#',end="")
        j=j+1
    i=i+1
    print()


#3.)perfect squares

i = 1

while i * i <= 500:
    print(i * i)
    i += 1
    
