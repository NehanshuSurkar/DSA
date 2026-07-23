def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)
sum(3)

if __name__ == "__main__":
    n = int(input("Enter the number of times to print the name: "))
    print(sum(n))