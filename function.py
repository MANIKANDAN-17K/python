def add(a = 2,b=3):
    return a + b
    
def diff(a=1,b=0):
    return a - b
def product(a=3,b=4):
    return a*b
    
print("sum",add(10,11))
print("diff",diff(10,2))
print("product",product(3,8))

print("sum",add())
print("diff",diff())
print("product",product())
