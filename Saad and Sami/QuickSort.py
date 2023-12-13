def quick_sort(array, p, r, index):
    if p < r:
        if r - p == 1:
            return
        q = partition(array, p, r, index)
        quick_sort(array, p, q - 1, index)
        quick_sort(array, q + 1, r, index)

def partition(array, p, r, index):
    x = array[r][index]
    i = p - 1
    j = p
    while j < r:
        try:
            y=float(array[j][index]) 
            x=float(x)
        except:
            y=array[j][index]
        if (y <= x ):
            i += 1
            array[i], array[j] = array[j], array[i]
        j += 1
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1

