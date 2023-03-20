print(type("hello world"))
username = 'supercoder'
password = 'supersecret'
long_string = '''
WOW 
0 0
---
'''

print(long_string)

first_name = 'mike'
last_name = 'skin'
full_name = first_name + ' ' + last_name
print(full_name)

# string concatenation 
print('hello ' + 'world')

# # will not work
# print('hello' + 5)

# --------------------------------

# type conversion
a=str(100)
b=int(a)
c=type(b)
print(c)

# same as above
print(type(int(str(100))))

# ---------------
# Escape Sequences

# \ = everything after this is a string 
# \t = tab
# \n = new line

weather = "\t It\'s \"kind of\" sunny \n hope you are having a good one!"

print(weather)