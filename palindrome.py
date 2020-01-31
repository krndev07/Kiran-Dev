a = int(input())
n = a
rev=0
while (n!=0):
    dig = n%10
    rev = rev*10+dig
    n=n//10
if rev == a :
    print("palindrome")
else:
    print("not a palindrome")
