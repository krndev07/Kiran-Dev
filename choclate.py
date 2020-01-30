import sys;


# arr[0..n-1] represents sizes of packets
# m is number of students.
# Returns minimum difference between maximum
# and minimum values of distribution.
def findMinDiff(arr, n, m):
    # if there are no chocolates or number
    # of students is 0
    if (m == 0 or n == 0):
        return 0

    # Sort the given packets
    arr.sort()

    # Number of students cannot be more than
    # number of packets
    if (n < m):
        return -1

    # Largest number of chocolates
    min_diff = sys.maxsize
    

    # Find the subarray of size m such that
    # difference between last (maximum in case
    # of sorted) and first (minimum in case of
    # sorted) elements of subarray is minimum.
    first = 0
    last = 0
    i = 0
    while (i + m - 1 < n):

        diff = arr[i + m - 1] - arr[i]
        if (diff < min_diff):
            min_diff = diff
            first = i
            last = i + m - 1

        i += 1

    return (arr[last] - arr[first])


# Driver Code
if __name__ == "__main__":
    arr = [12, 4, 7, 9, 2, 23, 25, 41,
           30, 40, 28, 42, 30, 44, 48,
           43, 50]
    m = 7  # Number of students
    n = len(arr)
    print("Minimum difference is", findMinDiff(arr, n, m))

