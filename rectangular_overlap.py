class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

def rectangular(l1,r1,l2,r2):
    if (l1.x>r2.x or l2.x>r1.x):
        return False
    if (l1.y<r2.y or l2.y<r1.y):
        return False
    return True
if __name__=="__main__":
    l1=point(0,10)
    r1=point(5,5)
    l2 = point(5, 5)
    r2 = point(15, 0)
    if rectangular(l1,r1,l2,r2):
        print("overlap")
    else:
        print("not")

