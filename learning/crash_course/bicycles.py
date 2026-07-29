# Ordered
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

# There are various prebuilt methods to use on lists

# Indexing
# You can use methods on any element in a list
print(bicycles[0].title())

# Modifying elements
bicycles[0] = "something"
print(bicycles[0])

# Appending elements
bicycles.append("another bike")
print(bicycles)

# Inserting into a list
bicycles.insert(0, "first element")
print(bicycles)

# Removing elements at certain index
del bicycles[0]
print(bicycles)

# Pop returns value after removing it
# Last element only
not_bicycles = bicycles.pop()
print(not_bicycles)

# You can specify an index to pop anything
also_not_a_bike = bicycles.pop(2)
print(also_not_a_bike)

# You can remove an item from its val 
# without having to know its index
# Use remove instead of del
bicycles.remove("cannondale")

# Remove only deletes the first occurence of a value 
# If it appears more than once you'd need to use a loop

