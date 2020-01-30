def duplicate(arr):
    arr.sort()
    print(arr)
    arr1=[]

    #print(len(arr))
    for i in range(0,len(arr)):
        if arr[i] not in arr1:


            arr1.append(arr[i])
    print(arr1)
arr=[18,7,1997,18,7,1998]
duplicate(arr)
