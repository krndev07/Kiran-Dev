nterms = int(input("How many terms? "))
# first two terms
n1, n2 = 0, 1
count = 0
count1=0
even=3
# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:

       nth = n1 + n2


       n1 = n2
       n2 = nth
       count += 1