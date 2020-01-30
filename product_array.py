def product(arr):
    sum=1
    for i in range(0,len(arr)):
        while i<len(arr):
              if  i<len(arr)-1:
                  sum = sum * arr[i+1]
              sum = sum * arr[i]

              i=i+1
        print(sum)







arr=[10,3,5,6,2]
product(arr)
