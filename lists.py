# lists

li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1,2, 'a', True]

# Data Structure

# ------------------------------

# List Slicing
amazon_cart = [
    "hellocopter", 
    "sun",
    'toys',
    'dinos'
    ]

# lists ARE NOT immutable - they have the ability to change

amazon_cart[0] = 'space ship'
# you can change any list item

new_cart = amazon_cart[0:3]
# BUT when you use list slicing, it creates a new list
new_cart[1] = 'REX'

newer_cart = amazon_cart[:]
# IF you want to "copy" a list, you have to SLICE IT with [:]
newer_cart[3] = 'hot dogs'

print(amazon_cart[1:3])
print(amazon_cart)
print(new_cart)
print(newer_cart)

# ------------------------------

# Matrix




