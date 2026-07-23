def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
fact(3)

if __name__ == "__main__":
    n = int(input("Enter the number to calculate factorial: "))
    print(sum(n))