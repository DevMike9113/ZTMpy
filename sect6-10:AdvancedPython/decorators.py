# # @classmethod
# # @staticmethod
#
# # functions are first class citizens
# # they can be passed all around
# # they act like variables
#
# def hello(func):
#     func()
#
#
# def greet():
#     print('still here')
#
#
# a = hello(greet)
#
# print(a)

# # --------------
#
# # higher order function HOC
# # functions that accept functions as a parameter
# def greet(func):
#     func()
#
#
# # function that returns another function
# def greet2():
#     def func():
#         return 5
#
#     return func()

# # --------------
#
# # a Decorator supercharges our function
# # its a function that wraps another function and enhances/changes it
#
# def my_dec(func):
#     def wrap_func():
#         print('yo')
#         func()
#
#     return wrap_func
#
#
# @my_dec
# def hello():
#     print('hello')
#
#
# # below is what a decorator does
# my_dec(hello)()
#
#
# @my_dec
# def bye():
#     print('bye')
#
#
# bye()
#
# hello()

# # ---------------

# Decorator Pattern
def my_dec(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)

    return wrap_func


@my_dec
def hello(greeting, emoji=':P'):
    print(greeting, emoji)


hello('hi')

# @my_dec
# def bye():
#     print('bye')
#
#
# bye()
