def partition(p, r):
    """Returns the position of the pivot with elements to left and right, lesser and greater respectively"""
    x  = A[r] # Pick last element as pivot
    i = p-1 # i marks the position of the last element less than pivot
    for j in range(p, r): # We dont have include r
        if A[j]  <= x: # if the current element is smaller than or equal to pivot
            i = i + 1
            # Exchange A of i and j
            A[i], A[j] = A[j], A[i]
        print(A)

    # Exchange A of i+1 and r
    A[i+1], A[r] = A[r], A[i+1]

    #Print A after partition
    print(A)
    # Return i+1
    return i+1
            
def quicksort(p, r):
    if p <= r:
        q = partition(p, r)
        quicksort(p, q-1)
        quicksort(q+1, r)

if __name__ == '__main__':
    A = [ 8, 1, 6, 4, 0, 3, 9, 5]
    quicksort(0, len(A)-1 )
