def closest(n,m):
    for i in range(n,2*n):
        if i%m==0:

            break
    for j in range(n-m,n):
        if i%m==0:

            break
    a = i-n
    b = n-j
    if a<b:
        print(i)
    else:
        print(j)
    return
    return
n= 15
m= 4
closest(15,4)




