n = int(input("Enter the ending value for factorial "))
fact = 1
for i in range(1,n+1):
    fact *= i;
print("the factorial of {} is {} ".format(n,fact))
 
