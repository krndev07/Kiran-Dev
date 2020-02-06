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
    def array(self,a):
        sum=""
        temp=self.head
        while temp:
            a.append(temp.data)
            temp=temp.next
        #print(a)
        kir="".join(a)
        for i in  kir:
            sum=i+sum
        if kir==sum:
            print("yes")
        else:
            print("no")
if __name__=="__main__":
    list1=linkedlist()
    list1.push("a")
    list1.push("bc")
    list1.push("d")
    list1.push("ba")
    a=[]
    list1.array(a)


