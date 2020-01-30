def minimum(arr):
    res=arr[0]
    for i in range(0,len(arr)):
        res=min(res,arr[i])
        return res


def maximum(arr):
    res1=arr[0]
    for j in range(0,len(arr)):
        res1=max(res1,arr[j])

    print(minimum(arr))
    print(res1)

arr=[14,10,1997,18,7,1998]

maximum(arr)
