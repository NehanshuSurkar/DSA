arr = [1,2,3,4,5]
# left = 0
# right = len(arr)-1
# def revv(arr, left, right):
#     if arr[left] >= arr[right]:
#         return
#     arr[left], arr[right] = arr[right], arr[left]
#     revv(arr, left+1, right-1) 
# revv(arr, left, right)
# print(arr)   

n = len(arr)
def rev(i):
    if i>=n//2:
        return
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    rev(i+1)
rev(0)
print(arr)       