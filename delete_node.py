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
    def dele(self,a):
        temp=self.head

        while temp:
            a.append(temp.data)
            temp=temp.next
        b=int(input("enter the node to delete: "))
        print(a)
        if b in a:
            a.remove(b)
        print(a)
        list2=linkedlist
        for i in range(0,len(a)):
            list2.push(self,i)
if __name__=="__main__":
    list=linkedlist()
    list.push(5)
    list.push(4)
    list.push(6)
    a=[]
    list.dele(a)




