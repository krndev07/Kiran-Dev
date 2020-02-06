class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=node(new_data)
        new_node.next=self.head
        self.head=new_node
    def list(self,a):
        temp=self.head
        while temp:
            a.append(temp.data)
            temp=temp.next


if __name__=="__main__":
    list1=linkedlist()

    list1.push(1)
    list1.push(2)
    list1.push(3)
    list1.push(4)
    list1.push(5)

    list2 = linkedlist()
    list2.push(5)
    list2.push(2)
    list2.push(3)
    list2.push(4)
    list2.push(5)
    a=[]
    b=[]
    list1.list(a)
    list2.list(b)
    print(a)
    print(b)
    x = int(input("enter the valve: "))

    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if a[i] + b[j] == x:
                print(a[i], b[j])







