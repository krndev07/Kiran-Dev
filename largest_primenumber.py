def prime(x):
    largest=0
    for i in range(2,x):
        if x%i==0:
            largest=i
        else:
            continue

    print(largest)

x=10
prime(10)

