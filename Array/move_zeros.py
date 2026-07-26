arr = [0,3,0,5,2,0,8]
index = len(arr) - 1

for i in reversed(arr):
    if i!=0:
        arr[index] = i
        index -= 1
while index > 0:
        arr[index] = 0
        index -= 1              
print(arr)