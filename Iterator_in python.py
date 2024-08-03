#61 Python Tutorial for Beginners | Iterator:..
nums=[7,8,9,5]

print(nums[3])
for i in nums:
    print(i)



#iterator:

it= iter(nums)#will convert  list into a itarator
print(it.__next__()) #if we print we get <list_iterator object at 0x000002587030BB50> we don't want it so that we use the method clled as __next__() so you will get the 1st number of the list

print(it.__next__()) # here behind the sence you say the iterator it will have the multiple values so you will say hey iterator and calling your method next now in this next it will pick up the one value so maybe there is a loop.

print(it.__next__())

#so it is used to do we  don't want to call with the index values by just keeping the above method we can iterate the values  

#we can use this method also:
print(next(it))

#what if you want to create a own iterator is it possible::
class TopTen:
    
    def __init__(self):
        self.num=1

    def __iter__(self): #this will give you the object
        return self

    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values=TopTen()

print(next(values))
for i in values:
    print(i)

    
    


#Let's see an example that will give us the next power of 2 in each iteration. Power exponent starts from zero up to a user set number,

class powTwo:

    def __init__(self,max=0):
        self.max=max

    def __iter__(self):
        self.n=0
        return self

    def __next__(self):
        if self.n<=self.max:
            res=2**self.n
            self.n+=1
            return res
        else:
            raise StopIteration


power=powTwo(10)
i=iter(power)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
#or use this also
for i in power:
    print(i)

        
        
