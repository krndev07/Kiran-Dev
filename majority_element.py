def major(arr):
    count=1

    n=len(arr)

    b=[]
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                count=count+1
            else:
                continue
            if count>=n//2:

                if arr[i] in b :
                    break
                else:
                    b.append(arr[i])
                    print(b)


arr=[3,1 ,3, 3, 2]
major(arr)