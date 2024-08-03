#70 Python Tutorial for Beginners | Bubble Sort in python | List Sort::..

#simple one:
nums=[5,3,8,6,7,2]
x=sorted(nums)
print(x)


#we are defining the sort function:

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

nums=[5,3,8,6,7,2]
sort(nums)
print(nums)             
