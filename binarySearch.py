from math import floor

def binarySearch(A, b, e, num):
    mid = int(floor((b+e)/2))
    if A[mid] == num:
        return mid
    elif b==e:
        return None
    elif A[mid] > num:
        return binarySearch(A, b, mid-1, num)
    else:
        return binarySearch(A, mid+1, e, num)

a = [1, 2, 3, 4, 5, 7]

print str(binarySearch(a, 0, len(a)-1, 7))
