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

def bucket_sort(arr, column_index):
    n = len(arr)
    max_value = float("-inf")
    min_value = float("inf")

    for i in range(n):
       
        if max_value< float(arr[i][column_index]):
            max_value = float(arr[i][column_index])
        if min_value> float(arr[i][column_index]):
            min_value = float(arr[i][column_index])

    num_buckets = n  
    bucket_range = (max_value - min_value) / num_buckets

    buckets = [[] for i in range(num_buckets + 1)]

    for i in range(n):
 
        element = float(arr[i][column_index])

        bucket_index = int((element - min_value) // bucket_range)
        if bucket_index >= num_buckets:
            bucket_index = num_buckets - 1
        buckets[bucket_index].append(arr[i])

    for i in range(num_buckets):
        insertion_sort(buckets[i], column_index,True)

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array


