
def repeating(arr):
    arr.sort()
    for i in range(0,len(arr)-1):
        if arr[i]==arr[i+1]:
            print(arr[i],"is repeating element")

arr=[4, 6, 2, 1, 1]
def missing(arr):
    arr.sort()
    n=0
    for i in range(0,len(arr)):
        n=n+1
        if n in arr:
            continue
        else:
            print(n,"is missing element")
repeating(arr)
missing(arr)




