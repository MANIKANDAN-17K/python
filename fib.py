n = int(input("Enter the ending value for fibonacci series "))
a,b,c = 0,1,0
print(f" {a} ",end=' ')

for i in range (1,n+1):
    c =a+b
    a =  b 
    b = c 
    print(f" {a} ",end = ' ')
