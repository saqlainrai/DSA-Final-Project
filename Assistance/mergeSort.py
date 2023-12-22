
def merge(A, p, q, r, index, ascending):
    nL = q - p + 1
    nR = r - q
    left = [0] * nL
    right = [0] * nR
    for i in range(nL):
        left[i] = A[p + i]

    for j in range(nR):
        right[j] = A[q + 1 + j]
    
    i = j = 0
    k = p
    while i < nL and j < nR:
        try:
            x=float(left[i][index]) 
            y=float( right[j][index])
        except:
            x=left[i][index]
            y=right[j][index]
        if (ascending and x <=y) or (not ascending and x >= y):
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    while i < nL:
        A[k] = left[i]
        i += 1
        k += 1

    while j < nR:
        A[k] = right[j]
        j += 1
        k += 1

def merge_sort(A, p, r, index, ascending):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q, index, ascending)
        merge_sort(A, q + 1, r, index, ascending)
        merge(A, p, q, r, index, ascending)
