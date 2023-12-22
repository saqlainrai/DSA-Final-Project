def quick_sort(array, p, r, index,assending):
    if p < r:
        if r - p == 1:
            return
        q = partition(array, p, r, index,assending)
        quick_sort(array, p, q - 1, index,assending)
        quick_sort(array, q + 1, r, index,assending)

def partition(array, p, r, index,assending):
    x = array[r][index]
    i = p - 1
    j = p
    while j < r:
        try:
            y=float(array[j][index]) 
            x=float(x)
        except:
            y=array[j][index]
        if (y <= x  and assending):
            i += 1
            array[i], array[j] = array[j], array[i]
        if (y >= x  and not assending):
            i += 1
            array[i], array[j] = array[j], array[i]
        j += 1
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1
a=[[1,0],[2,0],[3,0]]
quick_sort(a,0,2,0,False)
print(a)
quick_sort(a,0,2,0,True)
print(a)