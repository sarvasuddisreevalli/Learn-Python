# list[] -> mutable, more flexible
# tuple() -> immutable, faster
# set{} -> mutable (add/remove), unordered, no duplicates,best for membership testing

# List[]
fruits = ['orange','apple','grapes','papaya','orange']
print(fruits)
print(fruits[0])
fruits[2]='mango' # List is mutable
fruits.append('guava') # insert this element at end 
fruits.remove('orange') # removes first matches only 
fruits.pop(1) # pop element at that index
fruits.clear() # clear elements from list
for fruit in fruits:
    print(fruit,end=' ')

# Tuple()
fruits = ('orange','apple','grapes','papaya')
print(fruits)
print(fruits[0])
# fruits[2]='mango' # Immutable, so shows doesn't support item assignment for tuple
# fruits.append('guava') # Shows no attribute append for tuple
for fruit in fruits:
    print(fruit,end=' ')

# Set{}
# Best for membership testing means checking given element in set
fruits = {'orange','apple','grapes','papaya','orange'} # removes duplicates
print(fruits) # order changes for every single run
# print(fruits[0]) # doesn't work
# fruits[2]='mango' # Error: set doesn't support item assignment
# fruits.append('guava') # Shows set has no attribute append
fruits.add("pomegranate") # add new element to anywhere in set
fruits.remove("grapes") # delete element from set
# fruits.clear() # empty set
for fruit in fruits:
    print(fruit,end=' ')

fruit = input("Enter a fruit name to search in fruits set :")
if fruit in fruits:
    print(f"{fruit} was found")
else:
    print(f"{fruit} was not found")
