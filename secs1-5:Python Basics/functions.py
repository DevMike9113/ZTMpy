# # functions
# # DRY
# # define first then you can call the function

# def say_hello():
#     print ("hello")

# say_hello()

# #--------------

# # parameters and arguments

# # params - NAMES of the variables that the function RECEIVES - define
# def say_hello(name='butt', emoji=':0'): #default parameters
#     print (f"hello {name} {emoji}")

# # args - the VALUES that we PROVIDE to the function - call / invoke
# # positional arguments
# say_hello('Mike', ':)')

# # ----------

# # key word arguments
# say_hello(name='bibi', emoji=':p')

# say_hello() # default parameters

# # -----------------

# def sums(n1,n2):
#     def func(r1, r2):
#         return r1 + r2
#     return func(n1,n2)
    
# # function should do one thing really well
# # should return something

# total = sums(10,5)
# print(sums(4,total))

# # a return keyword automatically exits a function

# # ------------------

# # functions
# list()
# print()
# max()
# min()
# input()

# def something():
#     pass
# something()

# # methods have to be owned by something
# # the owner is whatever is to the LEFT of the .
# 'hello'.capitalize()

## --------------
# # '''
# # this is info about the function
# # '''

# # ---------------

# # args kwargs
# # star is a tuple

# def super_func(param, *args, i='default params', **kwargs):
#     total = 0
#     for items in kwargs.values():
#         total += items
#     return sum(args) + total

# print(super_func(1,2, num1=3, num2=10))

# # RULE: params, *args, default params, **kwargs

# # ----------

# # scope - what variables do i have access to?
# # a new world is essentially created when you create a new function

# # scope rules:
# # 1 - start with local within world
# # 2 - parent local
# # 3 - global
# # 4 - built in python functions 

# total = 0

# def count(total): # better than using the global key word
#     # global total 
#     total += 1
#     return total

# count()
# count()
# print(count())


# nonlocal makes it global
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner", x)
    inner()
    print("outer", x)
outer()