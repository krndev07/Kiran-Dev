def countSquares(m, n):
    # If n is smaller, swap m and n
    if (n < m):
        temp = m
        m = n
        n = temp

        # Now n is greater dimension,
    # apply formula
    return ((m * (m + 1) * (2 * m + 1) /
             6 + (n - m) * m * (m + 1) / 2))
if __name__=='__main__':
    m = 2
    n = 2
    print("Count of squares is "
         ,countSquares(m, n))
