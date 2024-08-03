#Linear Search using Python | Python Tutorial for Beginners 68::..

#By using the while loop:
pos=-1

def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False              


list=[5,8,4,6,9,2]
n=6

if search(list,n):
    print('found at',pos+1)
else:
    print('Not found')




#By using the for loop

pos = -1

def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
    return False

list = [5, 8, 4, 6, 9, 2]
n = 2

if search(list, n):
    print('found at', pos + 1)
else:
    print('Not found')
    
