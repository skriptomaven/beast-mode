# Dictionaries - collection of objects that store data in unordered {key:value} pairs.
# A key must be of a hashable & immutable data type and value can be any arbitrary
# Python object.
# Note: An object is hashable if it has a value that does not change during its
# lifetime in the program.
# Below is the syntax:
# dict = {
#   <key>: <value>,
#   <key>: <value>,
#   .
#   .
#   <key>: <value>
# }
# Keys are case-sensitive & cannot be duplicated
# Example:
my_dict = {
        '1': 'data',
        '2': 'structures',
        '3': 'Python',
        '4': 'Programming language'
        }
# Values in a dictionary can be fetched based on a key
print(my_dict['1']) # prints 'data'
# Create a sample dictionary
coder = {}
print(type(coder)) # prints: <class 'dict'>
coder['name'] = 'jeff'
coder['age'] = 27
coder['fav dish'] = 'fish'
print(coder) # outputs: {'name': 'jeff', 'age': 27, 'fav dish': 'fish'}
# Dictionaries allow operations below:

# in and not in
'age' in coder
'year' not in coder

# len(): finds length of a dict
len(coder)

# Remove all elements in a dict using: .clear()
coder.clear() # removes all elements in coder

# Search for key in a dict: .get(<key>)
coder.get('age') # get age in coder dict

# Return list if items in a dict: .items()
coder.items()

# List of keys use: .keys()
coder.keys()

# Return values use: .values()
coder.values()

# Remove a key use: .pop()
coder.pop()

# Remove the last key use: .popitem()
coder.popitem()

# Merge one dict with another use: .update(<obj>)
d_one = {'a': 10, 'b': 20, 'c': 30}
d_two = {'b': 200, 'd': 400}
new_d_one = d_one.update(d_two)
print(d_one) # returns: {'a': 10, 'b': 200, 'c': 30, 'd': 400}
