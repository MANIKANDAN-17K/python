s = {10, 20, 30, 40}

s.add(50)         # {10, 20, 30, 40, 50}
s.remove(20)      # {10, 30, 40, 50}
s.discard(100)    # No error if element not found
popped = s.pop()  # removes a random element
s.clear()         # empty set


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # Union → {1,2,3,4,5,6}
print(a & b)   # Intersection → {3,4}
print(a - b)   # Difference → {1,2}
print(a ^ b)   # Symmetric difference → {1,2,5,6}

