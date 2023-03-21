# print(type("hello world"))
# username = 'supercoder'
# password = 'supersecret'
# long_string = '''
# WOW 
# 0 0
# ---
# '''

# print(long_string)

# first_name = 'mike'
# last_name = 'skin'
# full_name = first_name + ' ' + last_name
# print(full_name)

# # string concatenation 
# print('hello ' + 'world')

# # # will not work
# # print('hello' + 5)

# # --------------------------------

# # type conversion
# a=str(100)
# b=int(a)
# c=type(b)
# print(c)

# # same as above
# print(type(int(str(100))))

# # --------------

# # Escape Sequences

# # \ = everything after this is a string 
# # \t = tab
# # \n = new line

# weather = "\t It\'s \"kind of\" sunny \n hope you are having a good one!"

# print(weather)

# # ---------------------

# # formatted strings
# name = 'Johnny'
# age = 55

# # f before string -- new feature in Py3
# # known as an f-string
# print(f'hi 1{name}. You are {age} years old')

# # old way
# print('hi 2{}. You are {} years old'.format(name, age))
# print('hi 3{0}. You are {1} years old'.format(name, age))
# print('hi 4{1}. You are {0} years old'.format(name, age))
# print('hi {new_name}. You are {age} years old'.format(new_name="sally", age=100))

# # --------------

# # string index - bookshelf
# selfish = 'abcdefgh'
#           #01234567 
# print(selfish[4])

# # [start:stop]
# print(selfish[3:5])

# # [start:stop:stepover]
# print(selfish[1:8:2])

# print(selfish[:5])
# print(selfish[2:])

# # reverse string
# print(selfish[::-1])
# # the above content is slicing

# # ---------------

# # immutablility
# # you cant change an existing string
# # you have to assign a completely new thing

# # --------------

# # Built in functions and methods

# # BI function example
# # len = length
# # len counts like humans from 1-9 not like computers from 0-8
# print(len('hello world')) # = 11 characters

# # BI Method example
# # .format is a method
# quote = 'to be or not to be'
# print(quote.upper())
# print(quote.capitalize())
# print(quote.find('be'))
# print(quote.replace("be", "me"))

# # ---------------

# # booleans
# name = 'Mike'
# is_cool = False
# is_cool = True

# print(bool(1)) # True
# print(bool(0)) # False

