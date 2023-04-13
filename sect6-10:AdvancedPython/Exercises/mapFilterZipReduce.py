from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalized(item):
    return item.upper()


cap_pets = list(map(capitalized, my_pets))
print('map', cap_pets)

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

my_numbers.reverse()

zipper = list(zip(my_numbers, my_strings))
print('zip', zipper)

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def fil_list(item):
    return item > 50


fil = list(filter(fil_list, scores))

print('filter', fil)


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def accumulator(acc, item):
    return acc + item


total_nums = my_numbers + scores

redo = reduce(accumulator, total_nums, 0)

print(total_nums)
print('reduce:', f'the total is {redo}')
