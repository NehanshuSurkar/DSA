s =  'babu'
n = len(s)
i  = 0
def palindrome(s, i, n):
    if i >= n//2:    
        return True
    if s[i] != s[n-i-1]:
        return False
    return palindrome(s, i+1, n)

print(palindrome(s,i, n))