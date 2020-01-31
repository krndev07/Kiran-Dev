import math

def factorial(x):
    res=1
    for i in range(2,x+1):
        res=res*i
    return res

def ncr(x,r):
    return (factorial(x)/(factorial(r)*factorial(x-r)))
x=5
r=3
print(ncr(x,r))


