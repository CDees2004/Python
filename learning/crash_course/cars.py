# Sorting
# You can sort alphabetically
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars_2 = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# You can also sort in reverse order 
cars_2.sort(reverse=True)
print(cars_2)

# Sorting permanently changes the list

# Sorted lets you display it in an order with no side effects
cars_3 = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars_3))
print(cars_3)

# Reverse method
print(cars.reverse())

# Finding length
print(f"The length of cars is {len(cars)}")

# Negative indexing 
# -1 always gives the last element
print(cars[-1])
