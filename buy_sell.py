def buy(arr):
    count=1
    if arr.sort(reverse = True)==arr:
        print("invalid")

    for i in range(0,len(arr)-1):

        if  arr[i]<arr[i+1]:
            count = count + 1
            count = count + 1

        else:
            print(i-count,count)
arr=[1,2,3,4,2,5]
buy(arr)