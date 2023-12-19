
def SelectionSort(array,index,asscending):
    for i in range(0,len(array)):
        for j in range(i,len(array)-1):
            try:
                x=float(array[j+1][index])
                y=float(array[i][index])
            except:
                x=array[j+1][index]
                y=array[i][index]
            if (x<y and asscending) or (x>y and not asscending) :
                temp = array[j+1]
                array[j+1]=array[i]
                array[i]=temp
