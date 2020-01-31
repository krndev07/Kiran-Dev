def factorial(x):

    return 1 if (x==1 or x==0) else x*factorial(x-1)
x=5
print(factorial(x))
