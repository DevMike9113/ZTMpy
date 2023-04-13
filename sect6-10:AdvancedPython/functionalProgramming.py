# # Functional Programming
# # separation of concerns
# # separate data and function
# # generally it is simplicity where data and functions are cconcerned
#
# # Clear and understandable
# # easy to extend
# # easy to maintain
# # memory efficient
# # DRY
#
# # PILLAR: Pure functions
#
# # ----------
#
# # F = [1,2,3]
#
# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item * 2)
#     return new_list
#
#
# tot = multiply_by2([1, 2, 3])
# print(tot)
#
# # pure functions are generally better code

# # --------------

# # map, filter, zip, reduce
#
# my_list = [1, 2, 3]
#
#
# def multiply_by2(item):
#     return item * 2
#
#
# tot = list(map(multiply_by2, my_list))
# print(tot)
# print(my_list)
#
# # map is useful for example: usernames. you can change it very easily

# # ----------------

# # map, filter, zip, reduce

# my_list = [1, 2, 3]
#
#
# def multiply_by2(item):
#     return item * 2
#
#
# def check_odd(item):
#     return item % 2 != 0
#
#
# tot = list(map(multiply_by2, my_list))
# fil = list(filter(check_odd, my_list))
#
# print(my_list)
# print('map', tot)
# print('filter', fil)

# # ---------

# # map, filter, zip, reduce

# my_list = [1, 2, 3]
# your_list = [10, 20, 30]
# their_list = (5, 4, 0)
#
#
# def multiply_by2(item):
#     return item * 2
#
#
# def check_odd(item):
#     return item % 2 != 0
#
#
# tot = list(map(multiply_by2, my_list))
# fil = list(filter(check_odd, my_list))
# zipper = list(zip(their_list, your_list, my_list))
#
# print(my_list)
# print('map', tot)
# print('filter', fil)
# print('zip', zipper)

# # ----------------

# # map, filter, zip, reduce

from functools import reduce

my_list = [1, 2, 3]


def accumulator(acc, item):
    print('acc, item', acc, item)
    return acc + item


# reduce(def_reducer, item/iterable[], initialVal
redoos = reduce(accumulator, my_list, 0)

print('reduce', redoos)
print('my list', my_list)
