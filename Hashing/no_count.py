n = int(input("enter number of elements in array: "))
arr = []
for i in range(n):
    arr.append(int(input("enter elements: ")))


hash_map = {}
for i in arr:
    if i in hash_map:
         hash_map[i] += 1
    else: 
        hash_map[i] = 1
        

q = int(input("enter number of queries: "))
while q > 0:
    number = int(input("enter number to check: "))

    print(hash_map.get(number,0))



    
