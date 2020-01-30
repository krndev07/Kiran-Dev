def trapping(arr):
    b=[]
    if arr[0]<arr[len(arr)-1]:
        comman=arr[len(arr)-1]-arr[0]
        comman=arr[len(arr)-1]-comman
    else:
        comman=arr[0]-arr[len(arr)-1]
        comman=arr[0]-comman
    for i in range(0,len(arr)):
        if arr[i]==comman:
            b.append(0)
        if arr[i]<comman:
            b.append(comman-arr[i])
        if arr[i]>comman:
            b.append(0)
    print(sum(b))
arr=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
trapping(arr)
