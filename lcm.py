def gcd(a,b):
    count=0

    for i in range(1,min(a,b)+1):
        if (a%i)==(b%i)==0:
            count = count+1
        else:
            continue

    print(count)
def lcm(a,b):
    (a*b) / gcd(a,b)
    return 
a = 15
b = 20
print('LCM of', a, 'and', b, 'is', lcm(a, b))