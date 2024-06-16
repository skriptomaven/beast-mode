# Data Structures and Algorithms

''' An algorithm: A set of step-by-step instructions to solve any given problem.
        - Algorithm processes the data and produces the output results based on the specific problem
        - The data used by the algorithm to solve the problem has to be stored & organized efficiently
        in the computer memory for the efficient implementation of the software.
        - The performance of the system depends upon the efficient access and retrieval of the data,
        and that depends upon how well the data structures that store & organize the data in the
        system are chosen.
        - Data structures deal with how the data is stored & organized in the memory  of the computer
        that is going to be used in the program.

    Data Types:
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
'''
