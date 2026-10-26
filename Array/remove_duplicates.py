def remove_duplicates(arr):
    pointer = 0

    for i in range(1,len(arr)):
        if arr[i]!=arr[pointer]:
            pointer +=1
            arr[pointer] = arr[i]
    return pointer+1


arr = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(arr))







