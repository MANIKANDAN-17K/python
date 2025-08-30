def isPalindrome(n):
    divisor =  1 
    while n // divisor > 10:
        divisor = divisor * 10
    
    while n > 10:
        left = n // divisor
        right = n % 10
        if left != right:
            return False
        n = (n % divisor) // 10
        divisor = divisor // 100
      
    return True
n = int(input("Enter the value of check the number is Palindrome or not "))
if isPalindrome(n):
    print(f"the given number {n} is Palindrome")
else:
    print(f"the given number {n} is not Palindrome")
