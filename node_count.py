class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head= None
    def count(self,a):

        temp=self.head
        while(temp):
            a=a+1
            temp=temp.next
        print(a)

if __name__=="__main__":
    list=LinkedList()
    list.head=node(1)
    list.second=node(2)
    list.third=node(3)

    list.head.next=list.second
    list.second.next=list.third
    a=0
    list.count(a)