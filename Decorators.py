#44 Python Tutorial for Beginners | Decorators
def div(a,b):
    if a<b:
        a,b=b,a
    return a/b
result=div(1,6)
print(result)

#using decorators you can add the extra features in the existing functions
def div(a,b):
    print(a/b)
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div=smart_div(div)
div(2,4)
