def digits(a,b,k):
    res = a**b
    count = 0
    while(res>0):
        dig=res%10
        res = res // 10
        count=count+1
        if count == k:
            return dig



res = digits(2,4,2)
print(res)


