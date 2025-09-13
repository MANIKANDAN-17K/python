fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


for i in range(5):  # 0 to 4
    print(i)

for i in range(1, 6):  # 1 to 5
    print(i)

for i in range(1, 10, 2):  # 1 to 9, step 2
    print(i)


i = 1
while i <= 5:
    print(i)
    i += 1

print("demo")
for i in range(1, 10):
    if i == 5:
        break
    print(i,end=' ')


print()
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
