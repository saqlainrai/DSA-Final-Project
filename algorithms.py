

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):                   # Last i elements are already in place
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swap function
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j 
        arr[i], arr[min_index] = arr[min_index], arr[i] # Swap function
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j] # Swap function
            j -= 1
        arr[j+1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2 # Finding the mid of the array
        L = arr[:mid] # Dividing the array elements
        R = arr[mid:] # into 2 halves

        merge_sort(L) # Sorting the first half
        merge_sort(R) # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1

        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1

        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1
    return arr

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)      # pi is partitioning index, arr[p] is now at right place
        quick_sort(arr, low, pi-1)          # Separately sort elements before partition and after partition
        quick_sort(arr, pi+1, high)
    return arr

def partition(arr, low, high):
    i = low-1 # index of smaller element
    pivot = arr[high] # pivot

    for j in range(low, high):
        if arr[j] <= pivot:
            i+= 1 # increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i] # Swap function

    arr[i+1], arr[high] = arr[high], arr[i+1] # Swap function
    return i+1

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # Swap function
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2*i+1 # left = 2*i+1
    r = 2*i+2 # right = 2*i+2

    # See if left child of root exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # Swap function
        heapify(arr, n, largest)

def counting_sort_p(input):
    l = min(input)
    k = max(input) - l
    for x in range(len(input)):
        input[x] -= l

    count =[0 for x in range(k+1)]
    for i in range(len(input)):
        count[input[i]] += 1

    for j in range(1, len(count)):
        count[j] += count[j-1]

    final = [0 for x in range(len(input))]
    for x in range(len(input)):
        ref = count[input[x]]-1
        count[input[x]] -= 1
        final[ref] = input[x]

    for x in range(len(final)):
        final[x] += l
    return final

def counting_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    range_of_values = max_value - min_value + 1
    # Create the count array to store the frequency of each value
    count = [0] * range_of_values
    # Populate the count array
    for value in arr:
        count[value - min_value] += 1
    # Reconstruct the sorted array from the count array
    sorted_arr = []
    for i in range(range_of_values):
        sorted_arr.extend([i + min_value] * count[i])
    return sorted_arr

def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    while max1//exp > 0:
        arr = counting_sort(arr)
        exp *= 10
    return arr

def bucket_sort_p(arr):
    min_val = min(arr)
    max_val = max(arr)

    num_buckets = 10

    bucket_range = (max_val - min_val) / num_buckets

    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        # Calculate the bucket index
        index = min(int((num - min_val) / bucket_range), num_buckets - 1)
        buckets[index].append(num)

    for i in range(num_buckets):
        buckets[i] = insertion_sort(buckets[i])

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

def bucket_sort(arr):
    bucket = []
    slot_num = 10 # 10 means 10 slots, each
    for i in range(slot_num):
        bucket.append([])

    # Put array elements in different buckets
    for j in arr:
        index_b = int(slot_num*j)
        bucket[index_b].append(j)

    # Sort individual buckets
    for i in range(slot_num):
        bucket[i] = sorted(bucket[i])

    # Concatenate all buckets into arr[]
    k = 0
    for i in range(slot_num):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k+= 1
    return arr

def shell_sort(arr):
    n = len(arr)
    gap = n//2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def index_sort(arr):
    n = len(arr)
    max_element = max(arr)
    min_element = min(arr)
    range_of_elements = max_element-min_element+1

    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(n)]

    for i in range(0, n):
        count_arr[arr[i]-min_element] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    for i in range(n-1, -1, -1):
        output_arr[count_arr[arr[i]-min_element]-1] = arr[i]
        count_arr[arr[i]-min_element] -= 1

    for i in range(0, n):
        arr[i] = output_arr[i]
    return arr

def cycle_sort(arr):
    writes = 0

    for cycle_start in range(0, len(arr)-1):
        item = arr[cycle_start]

        pos = cycle_start
        for i in range(cycle_start+1, len(arr)):
            if arr[i] < item:
                pos += 1

        if pos == cycle_start:
            continue

        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        writes += 1

        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start+1, len(arr)):
                if arr[i] < item:
                    pos += 1

            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
            writes += 1
    return arr

def binary_search(arr, low, high, x):
    if high >= low:
        mid = low + (high - low)//2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1

def main():
    pass

if __name__ == "__main__":
    main()