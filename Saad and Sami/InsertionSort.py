def insertion_sort(arr, column_index,asscending):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        try:
            x = float(key[column_index])
        except (ValueError, TypeError):
            x = key[column_index]

        while j >= 0:
            try:
                y = float(arr[j][column_index])
            except (ValueError, TypeError):
                y = arr[j][column_index]
            
            if (x < y and asscending)or(x > y and not asscending):
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key

