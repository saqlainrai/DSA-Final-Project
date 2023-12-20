
def bubble_sort(array, index,ascending):
    n = len(array)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i,):
            try:
                # x=float(array[j][index]) 
                # y=float(array[j + 1][index])
                x=array[j][index]
                y=array[j + 1][index]
            except:
                x=array[j][index]
                y=array[j + 1][index]
            if (x > y and ascending) or (x < y and not ascending):
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
