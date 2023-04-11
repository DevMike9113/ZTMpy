# # Dictionary
# # data type & data structure
# # dict will have a key and value
# dicts = {
#     'a' : 1, # key value pairs
#     'b' : [9, 'hi', False],
#     'c' : 'hello world',
#     'd' : True
# }
# # curly braces denotes a dictionary
# # dictionary is an unordered key value pair

# print(dicts['a'])
# print(dicts)

# my_list = [
#     {
#     'a' : 1, # key value pairs
#     'b' : [9, 'hi', False],
#     },
#     {
#     'c' : 'hello world',
#     'd' : True
#     }
# ]
# print("my_list:", my_list[0]['b'][1])

# # -------------------

# # a dictionary is not sorted
# # they hold more info than lists

# # -------------------

# # Dictionary Keys
# # need to have a special property = needs to be immutable
# # key cannot be a list
# # a key has to be UNIQUE - just once otherwise we overwrite it

# your_list = [
#     {
#     5 : 1, # key value pairs
#     False : [9, 'hi', False],
#     },
#     {
#     'c' : 'hello world',
#     'd' : True
#     }
# ]

# print(your_list[0][False][1]) 

## -------------------

# Dictionary Methods

user = {
    'c' : 'hello world',
    'd' : True
    }

# print(user.get('age')) 

# # if the value is not there use the default value
# print(user.get('boogers', 'if not there use snot!'))

# # another way to create a Dictionary that is NOT that common
# # dict(key=value)
# user2 = dict(name="Booger Brains")
# print(user2)

# # Dict Methods 2
# print('basket' in user2)
# print('d' in user)

# # keys, values, items, update, clear, copy
# print('c' in user.keys())
# print('hello world' in user.values())
# print(user.items()) # the whole dict
# print(user.update({'c': 'Tee'})) # if the updated key doesnt exist, it will create a new one: pretty handy
# user3 = user.copy()
# print(user3)
# print(user.clear()) # creates an empty dict
# # there are others found in documentation 
