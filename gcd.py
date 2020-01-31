def gcd(a,b):
    count=0

    for i in range(1,min(a,b)+1):
        if (a%i)==(b%i)==0:
            count = count+1
        else:
            continue

    print(count)
    return
gcd(15,20)

