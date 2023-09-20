# -*- coding: utf-8 -*-
"""
find duplicates in an array with values from 0 to len(array)-1
"""


def get_dups(array):
    ht = {}   # hash table to keep track of elements that encountered in a list
    dups = []
    for x in array:
        # print(x)
        if x in ht:
            # print(ht)
            dups.append(x)
        else:
            ht[x] = x
    # print(ht)
    print(dups)
    return list(set(dups))


print(get_dups([0, 2, 1, 2, 0, 0]))
