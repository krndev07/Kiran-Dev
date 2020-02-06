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
    def list1(self,a):

        temp=self.head
        while temp:
            a.append(temp.data)
            temp=temp.next
        a.sort()
        print(a)
        list2=linkedlist
        for i in range(0,len(a)):
            list2.push(self,i)
        


if __name__=="__main__":
    list=linkedlist()
    list.push(3)
    list.push(4)
    list.push(5)
    a=[]
    list.list1(a)
