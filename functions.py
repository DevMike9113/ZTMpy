# # functions
# # DRY
# # define first then you can call the function

# def say_hello():
#     print ("hello")

# say_hello()

# #--------------

# parameters and arguments

# params - NAMES of the variables that the function RECEIVES - define
def say_hello(name='butt', emoji=':0'): #default parameters
    print (f"hello {name} {emoji}")

# args - the VALUES that we PROVIDE to the function - call / invoke
# positional arguments
say_hello('Mike', ':)')

# ----------

# key word arguments
say_hello(name='bibi', emoji=':p')

say_hello() # default parameters