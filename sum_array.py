def sum(arr):
    sum=0
    for i in range(0,len(arr)):
        sum=sum+arr[i]
    print(sum)
n=int(input("enter the no of element: "))
arr=[]
for i in range(0,n):
    ele=int(input())
    arr.append(ele)
sum(arr)