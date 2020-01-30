def smaller(arr,k):
    arr.sort()
    count=0
    for i in range(0,len(arr)):
        if k>=arr[i]:
            count=count+1
    print(count)
arr=[14,10,1997,18,7,1998]
k=6
smaller(arr,k)
