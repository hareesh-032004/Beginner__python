#Printing Patterns in Python using the while loops:
i=1
while i<=5:
    print("#",end="")
    j=1
    while j<=5:
        print("#",end="")
        j=j+1
    i=i+1
    print()

#Printing Patterns in Python using the for loops:
for i in range(4):
    for j in range(4):
     print("#",end="")
    print()

#another pattern:
for i in range(4):
    for j in range(i+1): #here i represents rows and j rep- colums so i starts from the 0 we incremnet it by +1
     print("#",end="")
    print()



#another pattern
for i in range(4):
    for i in range(4-i):
     print("#",end="")
    print()




#questions on patterns::
#1.)1234    2.)APQR
#   234        ABQR
#   34         ABCR
#   4          ABCD

for i in range(4):
    for j in range(i,4):
     print(j+1,end="")
    print()



# Generate pattern similar to APQR, ABQR, ABCR, ABCD
str1='ABCD'
str2='PQR'
for i in range(4):
    print(str1[:i+1]+str2[i:])



# Left-Aligned Triangle:
for i in range(6):
    for j in range(i+1):
     print("*",end="")
    print()



# Right-Aligned Triangle:
n = 6
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)

    
#Full Triangle
n=6
for i in range(1,n+1):
    print(' '*(n-i)+'*'*(2*i-1))


#inverted Triangle
n=6
for i in range(n,0,-1):
    print(''*(n-i)+'$'*(2*i-1))



#Diomand
n=3
for i in range(1,n+1):
    print(''*(n-i)+'*'*(2*i-1))

for i in range(n-1,0,-1):
    print(''*(n-i)+'*'*(2*i-1))

