def sliding_window_sum(k, arr):
    window = sum(arr[:k])
    answer = window

    for i in range(k, len(arr)):
        window += arr[i]
        window -= arr[i-k]
        answer = max(window, answer)
    return answer
    
print(sliding_window_sum(4, [1,4,2,10,23,3,1,0,20]))    

