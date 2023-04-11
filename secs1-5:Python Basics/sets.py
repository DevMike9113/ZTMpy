# # sets
# # unordered collection of unique objects
# # if you have multiple of the same in the set it will only return one
# # it only returns the unique items
# my_set = {1,2,3,4,5,6,5}
# my_set.add(100)
# my_set.add(2) # not added because its not unique
# print(my_set) # only the first unique items are returned

# my_list = [1,2,3,4,5,6,5]
# # set_list = set(my_list)
# print(set(my_list))
# # created a new set from a list / removed all duplicates

# print(1 in my_set)
# print(len(my_set)) # duplicates are not counted

# # --------------

# # More methods of Sets
# test = {4,5,6,7,8,9}
# test2 = {8,9,10,11,12}

# # any duplicates between the two sets are not shown / only what is different
# # it tells you the difference with out changing
# print(test.difference(test2)) 

# # removes the item from the set
# print(test.discard(6))
# print(test)

# # same as the method .difference but it actually removes the differences and updates the set accordingly 
# test.difference_update(test2)
# print(test)

# # the items that match in the two sets are shown
# # print(test.intersection(test2))
# print(test & test2) # short hand - not often used

# # checks if the two sets have NOTHING in common
# print(test.isdisjoint(test2))

# # combines the sets but removed any duplicates
# # print(test.union(test2))
# print(test | test2) # short hand

# # subset and superset
# game = {8,9}
# gamestop = {8,9,10,11,12}
# print(game.issubset(gamestop))
# print(game.issuperset(gamestop))