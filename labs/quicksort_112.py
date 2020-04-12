
def quicksort(A, n, l):

    if n >= l:

        return
    q = partition(A, n, l)
    quicksort(A, n, q - 1)
    quicksort(A, q + 1, l)

def partition(A, n, l):
    q = j = n
    while j < l:
        if A[j] <= A[l]:
            A[q], A[j] = A[j], A[q]
            q += 1
        j += 1
    A[q], A[l] = A[l], A[q]

    return q
