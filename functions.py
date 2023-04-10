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

# -----------------

def sums(n1,n2):
    def func(r1, r2):
        return r1 + r2
    return func(n1,n2)
    
# function should do one thing really well
# should return something

total = sums(10,5)
print(sums(4,total))

# a return keyword automatically exits a function