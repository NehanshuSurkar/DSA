def move_zeros(arr):
    index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[index], arr[i] = arr[i], arr[index]
            index += 1
    return arr         

arr = [0,5,3,4,0,0,7]
print(move_zeros(arr))



def move_zeros(arr):
    index = len(arr) - 1
    for i in range(len(arr) -1,-1,-1):
        if arr[i] != 0:
            arr[index], arr[i] = arr[i], arr[index]
            index -= 1
    return arr         

arr = [0,5,3,4,0,0,7]
print(move_zeros(arr))