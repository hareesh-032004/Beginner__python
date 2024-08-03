#62 Python Tutorial for Beginners | Generators:::
#Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once.



def TopTen():
    yield 1 #yield is a special keyword which will make your function as a generator
    yield 3
    yield 7
    yield 9
   
    



values=TopTen()
print(values.__next__())#if we run we get add of generator <generator object TopTen at 0x0000020292597CC0> so print it use the __next__()
print(values.__next__())

for i in values:
    print(i)



#Top ten perfect square:

def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq #This yield will give the next next value
        n=n+1

val=topten()
for i in val:
    print(i)
    



#or we can do like this also:
sq_gen=(i*i for i in range(1,11))

for i in sq_gen:
    print(i)




# example to implement a sequence of power of 2 using an generator..
def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
nums=PowTwoGen(7)
for i in nums:
    print(i)
