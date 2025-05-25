#69 Python Tutorial for Beginners | Binary Search Using Python::..
#Binary search your values should be in sorted.
#If search value is smaller then change upper Bound and mid Becomes new upper bound


pos=-1

def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2

        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
                
    return False     
list=[4,7,8,1,45,99]
n=450
if search(list,n):
    print('its found at:',pos+1)

else:
    print('Not found in the given list')




print(int(eval(input('Enter the number to calculate:'))))    
