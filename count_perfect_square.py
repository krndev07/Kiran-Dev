def square(n):
    count=0
    for i in range(1,n):
        if i*i<=n:
            count+=1
            print(i,"is perfect square")
        else:
            continue
    print("total perfect squares is",count)
n=10
square(10)
