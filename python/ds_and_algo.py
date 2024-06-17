'''
    ============================
    DATA STRUCTURES & ALGORITHMS
    ============================

    ---------
    Algorithm
    ---------
        A set of step-by-step instructions to solve any given problem.
        - Algorithm processes the data and produces the output results based on the specific problem
        - The data used by the algorithm to solve the problem has to be stored & organized efficiently
        in the computer memory for the efficient implementation of the software.
        - The performance of the system depends upon the efficient access and retrieval of the data,
        and that depends upon how well the data structures that store & organize the data in the
        system are chosen.
        - Data structures deal with how the data is stored & organized in the memory  of the computer
        that is going to be used in the program.

    ----------
    Data Types
    ----------
        These are simple data types
        1. Numeric - Integer(int), float, complex
        2. Boolean - bool
        3. Sequency - String(str), range, list, tuple

        These are complex data types
        4. Mapping - dictionary(dict)
        5. Set - set, frozenset

    0. Strings - HAHAHAHA we all know what strings are just rem that they are immutable

    1. Range - Represents an immutable sequence of numbers
             - Returns a seq. of numbers starting from a given number to a number specified in the
             function argument.
             - It is mainly used in ```for``` and ```while``` loops
             - Use case:
                range(start, stop, step) e.g., print(list(range(20, 10, -2)))

    2. Lists - Are used to store multiple items in a variable.
             - Duplicate values are allowed
             - Items can be of different types
             - Items are enclose in [] and separated by a comma
             - Example:
                stupid_list = [2, 'Kayla', 'diel', 700]
             - Lists are mutable: elements can be: added, deleted, shifted, and moved within
             the list.

             - Properties of lists:
                - ordered
                - dynamic
                - list element can be an arbirtray set of objects
                - list element can be accessed through indexing: a[2]
                - lists also support slicing: a[2:3]
                - lists are mutable: elements can be updated by + or -
                - list operators: in, not in, +, *, lenc(), max(), min()

    ===========================================
    MEMBERSHIP, IDENTITY, and LOGICAL OPERATORS
    ===========================================

    1. Membership Ops - are used to test for an element membership in a sequence: ```in``` and ```not in```
        - in: tests if a value exists in a sequence.
            : returns ```True``` if it does and ```False``` if it does not.

            first_list = [1, 2, 3, 4]
            second_list = [7, 8, 9]

            if first_list[0] in second_list:
                print('Found ya!')
            else:
                print('Not found')

        - not in: returns ```True``` if an item is not in a list and ```False``` if found.

            target_suspect = 23
            list_of_suspects = [20, 2, 43, 100]

            if target_suspect not in list_of_suspects:
                print('Not here!)
            else:
                print('He is here!')

    2. Identity Operators - are used to compare objects: ```is``` and ```is not```
        - is: is used to check whether 2 objs refer to the same obj
        - note that is it way different to == equality check op

        first_list = []
        second_list = []

        if first_list == second_list:
            print('Both are equal')
        else:
            print('Both are not equal')

        if first_list is second_list:
            print('Both variables are pointing to the same object')
        
        else:
            print('Both variables are not pointing to the same object')

        third_list = first_list

        if third_list is second_list:
            print('Both are pointing to the same object')
        else:
            print('Both are not pointing to the same object')

        - is not: is used to check whether two variables point to the same object or not

        list_one = []
        list_two = []
        if list_one is not list_two:
            print('Both list one and list two variables are the same objects')
        else:
            print('Both list one and list two variables are not the same object')

    3. Logical operators: AND, OR, and NOT

        - AND: Both conditions are met
            a = 30
            b = 40
            if a > 10 and b > 10:
                print('Both variables are greater than 10')
            else:
                print('At least one of the variables is less than 10')

        - OR: At least one condition is met

            a = 1
            b = 2
            if a > 0 or b > 0:
                print('At least one of the variables is greater than zero')
            else:
                print('Both variables are less than zero')

        - NOT: returns True if object or operand is false, otherwise returns False

            a = 10
            if not a:
                print('Boolean value of a is false')
            else:
                print('Boolean value of a is True')
'''

# Tuples - are used to store multiple items in a single variable
#        - are immutable, unchangeable
#        - best for storing data that we do not intend to modify in the program
#        - syntax: tuple_name('item_one', 'item_two', 'item_three') see example below
my_tuple = ('Jeff', 11, True, 'male')
#       - supports operations such as:
#       - length using len()
print(len((2, 3, 'John')))
#       - Concatenation using +
print((2, 3)+(7, 9))
#       - Repetition using *
print((2, 1)*3)
#       - Membership using bool
print(3, in ('hello', 'exyx', 3)) # returns True
#       - Iteration using loops
for i in (1, 2, 3):
    print(i) # prints 1, 2, 3

# Tuples support zero-based indexing, negative indexing, and slicing
temp = ('hello', 'john', 'doe')
print(temp[1]) # prints john
print(temp[-2]) # prints john
print(temp[1:]) # prints john, doe

# Complex data types
