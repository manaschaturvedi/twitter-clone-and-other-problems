"""
Write a function that given a list of strings and an input string will return True if you can create
the input string from the list of strings and will return False if you cannot create the string from
the list.
"""

from itertools import permutations


def can_create(list_of_strings,input_string):
    all_permutations = []
    for x in range(1, len(list_of_strings) + 1):
        all_permutations.extend([''.join(p) for p in list(permutations(list_of_strings, x))])

    return True if input_string.replace(' ','') in all_permutations else False

print(can_create(['back','end','front','tree'],'backend'))