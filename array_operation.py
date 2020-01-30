def insert(arr,key):
    arr.append(key)
    print(arr)
def delete(arr1,key):
     arr1.remove(key)
     print(arr1)
def search(arr2,key):
    if key in arr2:
        print("yes")
    else:
        return False

arr=[14,10,1997,49,18,7,1998]
key=49
insert(arr,key)
delete(arr,key)
search(arr,key)
