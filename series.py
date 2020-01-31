def series(a,b,N) :

    for i in range(1,N+1) :
        ans = a+ (i-1) * b
        print(ans)
    return ans
a = 2
b = 5
N = 5
series(a,b,N)
print("the", N, "term of series is :",a+(N-1)*b)



