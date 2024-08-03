#user input taking input from the user
x=input()
y=input()
z=x+y
print(z)
# so if you run this code you wull not get any error just blank because user is expecting from you write so that you should menction the some thing in the ()
x=input("Enter the First Number:")
print(type(x)) # while you see the output it is giving the str type but it is integer write what we want to do now??

y=input('Enter the Second Number:')
z=x+y
print(z)
#if we run it we get teh output as x=3,y=5 z=35 we are getting because input function will give you always a string type what we want is integer but it is giving a string
#so we want to convert it into a integer lets see that

x=input("Enter the First Number:")
a=int(x)
y=input('Enter the Second Number:')
b=int(y)
z=a+b
print(z)
#can you think you are wasting the line of the code so to reduce the line of the code yo do x as the int then remove the a=int(x) vice versa
x=int(input("Enter the First Number:"))
y=int(input('Enter the Second Number:'))
z=x+y
print(z)


#if you want a char the what will you do lets do it
ch=input('Enter a char:')
print(ch) #so you entered a char k and it id printed suppose you entered a char like xyz then it will give you like a string but you want a char like right so that we can use of index[] values

#By using the index value you entered xyz you want y then it is in the index 1 so
ch=input('Enter a char:')
print(ch[1])

#here is some trick that you can do that here is in only ch=input('Enter a char:') by keeping the index value so that input will take your string but print value according to your index value
ch=input('Enter a char:')[5]
print(ch)


#so you want to solve the expression then you can do by 'eval' lets do it
exp=eval(input("Enter the Expression:"))
print(exp)

#write a code to find the cube of the number taking input from the user
num=int(input("Enter the number:"))
print(num**3)


