# Using curly braces
person = {"name": "Alice", "age": 25, "city": "Paris"}

# Using dict() constructor
person2 = dict(name="Bob", age=30, city="London")

# Empty dictionary
empty = {}


print(person["name"])    # Alice
print(person.get("age")) # 25

# get() returns None if key not found (instead of error)
print(person.get("job")) # None

person["job"] = "Engineer"   # Add new key-value
person["age"] = 26           # Update existing
print(person)
# {'name': 'Alice', 'age': 26, 'city': 'Paris', 'job': 'Engineer'}

person = {"name": "Alice", "age": 25, "city": "Paris"}

print(person.keys())    # dict_keys(['name','age','city'])
print(person.values())  # dict_values(['Alice',25,'Paris'])
print(person.items())   # dict_items([('name','Alice'),('age',25),('city','Paris')])

squares = {x: x**2 for x in range(5)}
print(squares)  # {0:0, 1:1, 2:4, 3:9, 4:16}
