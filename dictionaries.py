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

# -------------------

# a dictionary is not sorted
# they hold more info than lists

# -------------------

# Dictionary Keys
# need to have a special property = needs to be immutable
# key cannot be a list
# a key has to be UNIQUE - just once otherwise we overwrite it

your_list = [
    {
    5 : 1, # key value pairs
    False : [9, 'hi', False],
    },
    {
    'c' : 'hello world',
    'd' : True
    }
]

print(your_list[0][False][1]) 