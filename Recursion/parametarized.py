def func(i, sum):
    if i<1:
        print(sum)
        return
    func(i-1, sum + i)
func(3,0)    

