def counting_sort(arr, column_index):
    n = len(arr)
    max_value = float(-1000000000000)
    for i in range(n):
        element = float(arr[i][column_index])
        
        if element > max_value:
            max_value = element

    count = [0] * (int(max_value) + 1)

    for i in range(n):

        element = int(float(arr[i][column_index]))
        count[element] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [None] * n
    for i in range(n - 1, -1, -1):
        element = int(float(arr[i][column_index]))

        output[count[element] - 1] = arr[i]
        count[element] -= 1
    for i in range(n):
        arr[i] = output[i]


