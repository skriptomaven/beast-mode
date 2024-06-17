# A set - is na unordered collection of hashable objects.
#       - iterable, mutable & has unique elements.
#       - order of elements is not defined
#       - items within the set must be immutable & hashable.
#       - supports membership testing operators: ```in```, ```not in```.
#       - also supports: intersection, union, difference, symmetric differences.
#       - sets cannot contain duplicate items.
#       - creation: 1. set() or 2. {}
sample_set_one = (['and', 'python', 'data', 'structures'])
sample_set_two = {'and', 'python', 'data', 'structures'}
#       - operations on sets:
#       1. intersection: & or .intersection()
sample_set_one.intersection(sample_set_two)
sample_set_one & sample_set_two
#       2. union: | or .union()
sample_test_one | sample_test_two
sample_test_one.union(sample_test_two)

#       3. difference between sets: - or .difference()
sample_test_one - sample_test_two
sample_test_one.difference(sample_test_two)

#       4. symmetric difference: ^ or .symmetricdifference()
sample_test_one ^ sample_set_two
sample_set_one.symmetricdifference(sample_set_two)

#       - Test whether a set is a subset of another use: .issubset()
sample_set_one.issubset(sample_set_two)

# Immutable Sets - Are just like sets but are immutable: frozensets

# frozensets - are useful when we want to use a set but require the use of an immutable object. 
#            - (purely my own understanding): used to create a set of sets
x = frozenset(['data', 'python', 'and', 'structures'])

a1 = frozenset(['data'])
a2 = frozenset(['structure'])
a3 = frozenset(['python'])
x = {a1, a2, a3}
