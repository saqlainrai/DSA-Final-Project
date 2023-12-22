
def shellSort(array,colum,assending):

    interval = len(array) // 2
    while interval > 0:
        for i in range(interval, len(array)):
            temp = array[i]
            j = i
            try:
                x=float(temp[colum])
                y=float(array[j - interval][colum])
            except:
                x=temp[colum]
                y=array[j - interval][colum]
            
            while j >= interval and  ((y> x and assending) or(y< x and not assending)):
                try:
                    x=float(temp[colum])
                    y=float(array[j - interval][colum])
                except:
                    x=temp[colum]
                    y=array[j - interval][colum]
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

