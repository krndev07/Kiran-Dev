def pairs(arr,sum):
    b=[]
    for i in range(0,len(arr)):
        for j in range(1,len(arr)):
            if i==j:
                break
            if arr[i]+arr[j]==sum:
                print(arr[i],arr[j])



arr=[1,2,3,4,5,6,7,]
sum=8
pairs(arr,sum)