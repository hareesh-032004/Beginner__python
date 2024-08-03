#Here we have some statements they are if,elif esle statements
#if: we have block of statements in if if its true then it will print else not print (if is bacically a block and in python we call them as the Suite where you can write the multiple statements)
if True:
    print("Iam True")
print("Iam False")##This statement not belongs to the if statement its not following the indentation means spaces by default you will get 4 spaces so use that 4 spaces only


#checking the number is even or odd
x=19
r=x%2
if r==0:
    print("Even") #if it is even then it will print

if r==10:
    print("Odd") #if it is odd then it will print
# in this above case it is checking the both if it is even also it will check odd one also r==1; we dont want it write, to check that it not make any snence as a programmer you have to see that so then use 'else:' we can check it by debug if it is even if will get out of that it will not check the odd casex=19 so by doing this we can improve the performance
x=22  
r=x%2
if r==0:
    print("Even")

else:
    print("Odd")


#Nested if case inside if another if
x=3  
r=x%2
if r==0:
    print("Even")
    if x>5:
        print("Greater than 5")
    else:
        print("Not greater than 5")

else:
    print("Odd")    


#elif
day=int(input('Enter a day:'))

if day==1:
    print('Monday')

if day==2:
    print('Tuesday')

if day==3:
    print('wednesday')

if day==4:
    print('Thursday')

if day==5:
    print('Friday')

if day==6:
    print('saturday')

if day==7:
    print('Sunday')

# if we run it and enter the number you want suppose 2 then i will check after the 2 also when we debug and check it as a programer we don't want it so do 'elif' then if you enter the 2 then it will print the data in it then get out of that so you can improve the performance

day=int(input('Enter a day:'))

if day==1:
    print('Monday')

elif day==2:
    print('Tuesday')

elif day==3:
    print('wednesday')

elif day==4:
    print('Thursday')

elif day==5:
    print('Friday')

elif day==6:
    print('saturday')

elif day==7:
    print('Sunday')

else:
    print("Wrong Day Please enter the another day value")

#here it it execute the value you entered suppose you entered the value 3 then it will 1,2,3 then it will get out of that so that we can improve that performance    
