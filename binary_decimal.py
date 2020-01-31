x =int(input("ENTER THE NUMBER :"))
count = 0
res = 0
while (x!=0):
        dig = x%10
        res = res + (dig*2**count)
        count=count+1
        x=x//10

print(res)
