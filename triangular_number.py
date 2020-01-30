# Returns True if 'num' is triangular, else False
def isTriangular(num):
    # Base case
    if (num < 0):
        return False

    # A Triangular number must be  
    # sum of first n natural numbers 
    sum, n = 0, 1

    while (sum <= num):

        sum = sum + n
        if (sum == num):
            return True
        n += 1

    return False


# Driver code
n = 55
if (isTriangular(n)):
    print("The number is a triangular number")
else:
    print("The number is NOT a triangular number") 