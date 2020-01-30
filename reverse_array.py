def reverse(arr,arr1):
    n=len(arr)
    b=1
    for i in range(0,n):
        arr1.insert(i,arr[n-b])
        b=b+1

    print(arr1)

arr=[14,10,1997,18,7,1998]
arr1=[]

reverse(arr,arr1)



#METHOD2




def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1


# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)
