# a for loop allows us to iterate over anything that has a collection of items 
user = {
    'name': 'Golem',
    "age": 5006,
    'can_swim': False
}

# # use the .items , .keys , .values methods

# # for item in user.items():
# #     # for x in [1,2,3,4]:
# #         print(item)
# # for item in user.keys():
# #     # for x in [1,2,3,4]:
# #         print(item)
# # for item in user.values():
# #     # for x in [1,2,3,4]:
# #         print(item)

# for key, value in user.items():
#         print(key, value)

# # iterable - list, dict, tuple, set, string
# # iterate - one by one check each item in collection

# # ----------
# # range
# for _ in range(0, 10, 3):
#     print(_)

# # ----------

# enumerate
for i, char in enumerate(list(range(100))):
      if char == 50:
            print(f'index of 50 is: {i}')