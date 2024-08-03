#63 Python Tutorial for Beginners | Exception Handling::..

#Errors is of three Types :1.complie time error, 2.Logical error, 3.Run time Error

#1.)Compile time Errors:
               #syntatical errors
               #ex:missing(:) wrong speeling of print




#2.)Logical errors:
                #code is working nothing wrong with the syntax everything is working but then when a user says hey i want to add two numbers 2+3=5 but it is giving the 4 that's the logical error **(wrong output)**




#3.)Runtime error:
              #code get's compiled nothing wrong with that syntax is aslo not showing any error and it is not giving the logical error as well everything is working
              # if we want to divide a two numbers 5/6 it will work what if 5/0 then we get an error at runtime in between we are getting an error
            


a=5
b=2
#k=int(input('Enter a number:'))
#print(k) #ValueError: invalid literal for int() with base 10: 'p'

try:
    print('Resourse open')
    print(a/b) #here we have an Normal st->5/2(will not give any error) and critical st->5/0(will get an error
    k=int(input('Enter a number:'))
    print(k)#if we print it outside the try block
    #print('resourse closed')#if we got exception then we connot close this ex:5/0 when this 5/0 is came it will open a file since a/b is getting an error it will directly go to the except block it will not go to closed resourse so keep this in the except block then it will work
    
#ZeroDivisionError: division by zero

except ZeroDivisionError as e:    
#except Exception as e:we can use this also Exception is used to all the exceptions
    print('Hey, you cannot divide by zero',e)#if you want to print what is the error the use Exception as e

    #print('Resouse is closed')#if we say 5/2 we not get resourse is closed so we should keep both in try and expect closed resourse noo..... because python gives us on more feature called as finally::.


except ValueError as e:
    print('Invalid Input')


except Exception as e:#This exception will handle the all the other errors not 0 division and value error
    print('something went wrong....')
#print('Bye')# here Bye is also not printing because execution is stopping in between we dont want that to solve that problem we have to use the special block called try

finally: # finally block will be executed if we got an error as well as if we don't get the error
    print('Resourse is closed')
    


#if we do 5/2 it will give output it will not check the except block ,except block checks only if there was a error
#when you open a file you should close a file before exiting











#example:

# define Python user-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass

# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
        
except InvalidAgeException:
    print("Exception occurred: Invalid Age")    
