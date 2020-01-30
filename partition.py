def part(arr,a,b):
    c=[]

    for i in range(0,len(arr)):
       if arr[i]<a:
           c.append(arr[i])

    for j in range(0,len(arr)):
        if arr[j]>=14 and arr[j]<=20:
            c.append(arr[j])
    for z in range(0,len(arr)):
        if arr[z]>b:
            c.append(arr[z])
    print(c)

arr=[1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
a=14
b=20
part(arr,a,b)

