# # lists

# li = [1,2,3,4,5]
# li2 = ['a', 'b', 'c']
# li3 = [1,2, 'a', True]

# # Data Structure

# # ------------------------------

# # List Slicing
# amazon_cart = [
#     "hellocopter", 
#     "sun",
#     'toys',
#     'dinos'
#     ]

# # lists ARE NOT immutable - they have the ability to change

# amazon_cart[0] = 'space ship'
# # you can change any list item

# new_cart = amazon_cart[0:3]
# # BUT when you use list slicing, it creates a new list
# new_cart[1] = 'REX'

# newer_cart = amazon_cart[:]
# # IF you want to "copy" a list, you have to SLICE IT with [:]
# newer_cart[3] = 'hot dogs'

# print(amazon_cart[1:3])
# print(amazon_cart)
# print(new_cart)
# print(newer_cart)

# # ------------------------------

# # Matrix
# matrix = [
#     [1,2,3],
#     [3,4,5],
#     [0,6,7]
# ]

# print(matrix[0] [2])

# # ------------------------------

# # list methods
# basket = [1,2,3,4,5]
# print("the number of items in the list is", len(basket))

# # adding method
# basket.append(100)
# basket.insert(3, 92)
# basket.extend([94, 34])
# new_list = basket
# print('basket', basket)
# # print('new list', new_list)

# # removing
# basket.pop()
# basket.pop(1)
# print('basket pop', basket)
# # pop removes the index

# basket.remove(92)
# # remove erases the actual value you type in
# # remove doesnt return a value, it simply changes

# print('basket remove', basket)

# cleared = basket.clear()
# # clears basket

# print('basket cleared', basket)

# # ------------------------

# # List Methods 2
# # index
# baskets = ["a",'b','e','a','f','g']

# print(baskets.index('e', 0, 5))
# print('is it in there?', 'x' in baskets)
# print('how many times is it in there?', baskets.count('a'), 'times!')

# # --------------------------

# # List Methods 3
# tubs = ["a",'b','e','a','f','g']
# # print(tubs.sort()) # produces nothing

# # tubs.sort()
# # modifies the basket in place

# print(tubs)

# print(sorted(tubs))
# # creates a new copy of list and sorts it

# new_tub = tubs.copy()
# # new_tub = tubs[:]
# new_tub.sort()
# new_tub.reverse()
# print('sorted, reversed, list', new_tub)

# # ------------------------

# # Common List Patterns
# print(len(new_tub))
# print(new_tub[::-1])

# print(list(range(1,20))) # generates a list very quickly

# sentence = ''
# sentence_new = sentence.join(['hi', 'hello', 'goodbye'])

# # ---------------------

# # list unpacking
# e,f,g, *other, d= [4,5,6,7,8,9,0]
# a,b,c = 1,2,3
# print(a)
# print(b) 
# print(c)
# print(e)
# print(f) 
# print(g)
# print(other)
# print(d)

# # -------------------

# # None
# # special data type - absence of value
# weapons = None
# print(weapons)

# # --------------------
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