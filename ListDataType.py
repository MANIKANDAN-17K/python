numbers = [1, 2, 3, 4, 5]
mixed   = [1, "hello", 3.14, True]
nested  = [[1, 2], [3, 4]]
empty   = []

fruits = ["apple", "banana", "cherry"]

print(fruits[0])    # "apple" (indexing starts at 0)
print(fruits[-1])   # "cherry" (last element)
print(fruits[1:3])  # ["banana", "cherry"] (slicing)


print(fruits)

fruits[1] = "abe"
print(fruits)
fruits.append("xyz")
print(fruits)
fruits.insert(1,"mani")
print(fruits)
fruits.remove("apple")
print(fruits)
print(fruits.pop())

squres = [x**2 for x in range(5)]
print(squres)

matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[1][0])  # 3
