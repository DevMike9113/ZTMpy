# file I/O
# input something from the outside world
# output something from the inside world
#
# my_file = open('test.txt')
# print(my_file.read)
# print(my_file.read)  # open is like a cursor. you can read it once but then its at the end of the file
#
# my_file.seek(0)
# print(my_file.read)
# print(my_file.readline)
# print(my_file.readlines())
#
# my_file.close()

# # ---------------
#
# # proper way to work with files
# # reading
# with open('test.txt', mode='r') as my_file:
#     print(my_file.readlines())
#
# # write to the file = assumes that its a new file
# # if the file doesn't exist 'w' will create it
# with open('test.txt', mode='w') as my_file:
#     text = my_file.write('hey its me')
#     print(text)
#
# # read and write = overwrites from the start
# with open('test.txt', mode='r+') as my_file:
#     text = my_file.write('boog')
#     print(text)

# # adds to the end of the text
# if the file doesn't exist 'a' will create it like 'w'
# with open('test.txt', mode='a') as my_file:
#     text = my_file.write(' boogie')
#     print(text)

# # -----------------
#
# with open('./testio/test.txt', mode='r') as my_file:
#     print(my_file.read())
#
# # pathlib
#
# # -----------

try:
    with open('./testio/test.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise err
