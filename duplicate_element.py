def find(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                print(arr[i])
    
arr=[1,2,5,1,4,2,3,4,5,3]
find(arr)