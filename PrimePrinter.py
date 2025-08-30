import math

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
        
    for i in range (3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            return False
            
    return True
    
n = int(input("Enter the number is prime or not : "))
for i in range(n):
    if isPrime(i):
        print(f"{i} ",end = ' ')
