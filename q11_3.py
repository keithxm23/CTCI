
#Q 11.3
#Find the number of times that an array has been shifted.
from math import floor

def binarySearch(A, b, e, num):
    mid = int(floor((b+e)/2))
    if A[mid] == num:
        return mid
    elif b==e:
        return None
    elif (num == A[mid]):
        return mid
    elif (A[b] <= A[mid]):
        if (num > A[mid]):
            b = mid+1
        elif (num >= a[b]):
            e = mid-1
        else:
            b = mid+1
    elif (num < A[mid]):
       e = mid-1
    elif (num <= A[e]):
       b = mid+1
    else:
       e = mid - 1

a = [8, 9,  1, 2, 3, 4, 5, 7]

for x in a:
    print str(x) + " :: " + str(binarySearch(a, 0, len(a)-1, x))

#print str(x) + " :: " + str(binarySearch(a, 0, len(a)-1, x))
