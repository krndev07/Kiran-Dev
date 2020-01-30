def longest(arr):
    count=1
    arr.sort()
    b=[]
    for i in range(0,len(arr)-1):
        if  arr[i+1]==arr[i]+1:
            count=count+1
        else:
            b.append(count)
            count=1




    print(max(b))
arr=[1, 9, 3, 10, 4, 20, 2]
longest(arr)