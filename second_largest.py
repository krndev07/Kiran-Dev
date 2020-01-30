def second(arr):
    first=ans=-1
    if len(arr)<2:
        print("invalid input")
    for i in range(0,len(arr)):
        if arr[i]>first:
            ans=first
            first=arr[i]
        elif(arr[i]>ans and arr[i]!=first):
            ans=arr[i]
    if ans==-1:
        print("no")
    else:
        print(ans)

arr=[14,10,1997,18,7,1998]
second(arr)