def func(i, n):
    if i > n: 
        return
    print(i)
    func(i + 1, n)
a = int(input("Enter the number of times to print the name: "))
func(1, a)    