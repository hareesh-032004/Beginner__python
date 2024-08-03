num=int(input("Enter the number:"))
for i in range(2,num):
    if num%2==0:
        print('Its not a prime')
        break
else:
    print("Its a prime") # here we het the output as 5 times it's a prime so we dont want that write so keep the else in the indentation of for and put break for the if, if it is prime we dont want it to check write...
        


#another method:
num = int(input("Enter the number: "))

if num <= 1:
    print("It is not a prime number")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")
    



        
    
