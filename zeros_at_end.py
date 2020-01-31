a = [1,0,5,0,2,0,0,1,0]
b=[]
c=0
count=0
for i in range(0,len(a)):
    if a[i]==0:
        count = count+1
    else:
        b.insert(c,a[i])
        c=c+1
for i in range(1,count+1):
    b.append(0)
print(b)
