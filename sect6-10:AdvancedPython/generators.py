# # Generators
# # key word: allows us to generate a sequence of values over time
# range(100)  # makes it one by one
# # range() is a generator
#
# # lives in the memory and takes up space
# list(range(100))  # creates a giant list and then stores it
#
#
# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i * 2)
#     return result
#
#
# # makes a list ^
# my_list = make_list(10)
# print(my_list)

# # --------------
#
# # iterable - any object that is able to loop through
# # __iter__
# # iteration is the act of taking an item from an iterable, do something with it, and then go on to the next one
# # loops we call that iteration, it's the processes itself
# # generators are actually all iterable
# # everything that is iterable though is NOT a generator.
# # a generator is a subset of iterable
# # difference between a generator and a regular iterable is how we implement them
#
# def generator_function(num):
#     for i in range(num):
#         yield i  # pauses until its told to go again
#
#
# #       comes back to it when next() is called
#
# g = generator_function(10)
# next(g)
# next(g)
# print(next(g))
#
# n = generator_function(1)  # you get a StopIteration error when the number exceeds the set function iteration
# next(n)
# print(next(n))
#
# # for item in generator_function(100):
# #     print(item)
#
# # -----------------

# from time import time
#
#
# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, **kwargs)
#         t2 = time()
#         print(f'took {t2 - t1} s')
#         return result
#
#     return wrapper
#
#
# @performance
# def long_time1():
#     print('1')
#     for i in range(10000000):  # range()
#         i * 5
#
#
# @performance
# def long_time2():  # twice as long as range()
#     print('2')
#     for i in list(range(10000000)):  # list()
#         i * 5
#
#
# long_time1()
# long_time2()
#

# def gen_fun(num):
#     for i in range(num):
#         yield i
#
#
# for item in gen_fun(10):
#     print(item)
#
# # ---------------------

# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             print(next(iterator))
#         except StopIteration:
#             break
#
#
# special_for([1, 2, 3])

# UNDER THE HOOD OF GENERATORS
# RANGE
class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 10)
for i in gen:
    print(i)
