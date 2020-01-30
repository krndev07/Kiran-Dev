def divisor(n):
    a=1
    for i in range(1,n):
        while (i<=n):
            if a%i==0:
               a=a+1
               i=i+1
               print(a)




n=3
divisor(10)


