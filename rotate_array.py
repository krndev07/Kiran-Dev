def rotate(arr,k):
    index=0
    n=0
    arr.sort()
    arr1=[]
    print(arr)
    for i in range(0,len(arr)):
        if i>=k:
            arr1.insert(index,arr[i])
            index=index+1

        elif k>i:
            arr1.append(arr[i])

    print(arr1)
arr=[14,10,1997,18,7,1998]

k=2
rotate(arr,k)
