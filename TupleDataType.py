t1 = (1, 2, 3)              # normal tuple
t2 = ("apple", "banana")    # string tuple
t3 = (1, 2, 3, "hi", 3.14)  # mixed tuple
t4 = (10,)                  # single element tuple → note the comma!
t5 = tuple([1, 2, 3])       # from list
fruits = ("apple", "banana", "cherry")

print(fruits[0])    # apple
print(fruits[-1])   # cherry
print(fruits[1:3])  # ('banana', 'cherry')


t = (1, 2, 3)
t = t + (4, 5)
print(t)  # (1, 2, 3, 4, 5)

person = ("Alice", 25, "Engineer")

name, age, job = person   # unpacking
print(name)   # Alice
print(age)    # 25
print(job)    # Engineer
nested = ((1, 2), (3, 4))
print(nested[1][0])   # 3
