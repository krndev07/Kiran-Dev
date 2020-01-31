def zero(arr, n) :
    count = 0
    for i in range(n) :
        if arr[i]!=0:
            arr[count] = arr[i]
            count+=1
    while count<n:
        arr[count] = 0
        count+=1
arr= [1.2,4,6,0,0,6,0,5]
n = len(arr)
zero(arr,n)
print(arr)

