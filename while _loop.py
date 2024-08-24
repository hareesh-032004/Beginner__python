#while loops and for loops are used to do some iteratios so if you want to print the Naresh 1000 times what you do??
#would you write 1000 times print Naresh no in this case we use while or for loops let'see that
#for every thing we count from 1 write so

i=1 #initialization 
while i<=100: # condition
    print("Naresh",i)#here we can print the values also by keepingm i
    i=i+1 #increment/decrement

#decrement
i=50
while i>=1:
    print("NANI",i)
    i=i-1



#here we can use the multiple while loops this can also called as Nested while loops
i=1
j=1
while i<=5:
    print("Hareesh")
    while j<=4:
        print("Srikanth")
        j=j+1
    i=i+1
#here if we see the output:
#Hareesh
#Srikanth
#Srikanth
#Srikanth
#Srikanth
#Hareesh
#Hareesh
#Hareesh
#Hareesh
# so here we got first outer loop as first then it will go inside the loop then it will print the inner loop then after reached the iiner condition then it will go to the outer while loop that why we got that output


i=1
while i<=5:
    print("Hareesh",end="")
    j=1
    while j<=4:
        print("Srikanth",end="")
        j=j+1
    i=i+1
    print()

#output:
 # HareeshSrikanthSrikanthSrikanthSrikanth
 # HareeshSrikanthSrikanthSrikanthSrikanth
 # HareeshSrikanthSrikanthSrikanthSrikanth
 # HareeshSrikanthSrikanthSrikanthSrikanth
 # HareeshSrikanthSrikanthSrikanthSrikanth

    
