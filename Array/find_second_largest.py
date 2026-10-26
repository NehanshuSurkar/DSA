def second_largest(arr):
    arr.sort()

    largest = arr[-3]

    for i in range(len(arr)-2, -1, -1):
        if arr[i] < largest:
            return arr[i]
    return -1
arr = [12, 35, 50, 1, 10, 34, 1]
print(second_largest(arr))