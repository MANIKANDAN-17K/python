def reverse(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev
n = int(input("Enter the value for reverse the number : "))
print(f"The orginal number is {n} its reverse format is {reverse(n)}")
