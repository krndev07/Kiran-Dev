def maxi(arr):
    sum=[]
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                sum.append(j-i)
    if sum==[  ]:
        print(-1)
    else:
        print(max(sum))
arr=[6, 5, 4, 3, 2, 1]
maxi(arr)
