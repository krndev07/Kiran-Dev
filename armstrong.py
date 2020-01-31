x=500
result = 0

while (x != 0) :
    remainder = x % 10
    result +=remainder*remainder*remainder
    x/=10



if (x == result):
    print("arm")
else:
    print("not")