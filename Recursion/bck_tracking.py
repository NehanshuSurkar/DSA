def func(i, n):
    if i < 1: 
        return
    func(i - 1, n)
    print(i)
a = int(input("Enter the number of times to print the name: "))
func(a, a)    