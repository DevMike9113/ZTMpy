# # walrus operator
# # assigns values to variables as part of a larger expression
# a = 'hello world'
#
# # w/o walrus
# if (len(a) > 10):
#     print(f"too long, {len(a)} elements")
#
# # WITH walrus
# if ((n := len(a)) > 5):
#     print(f"too long, {n} elements")
#
# while ((n := len(a)) > 1):
#     print(n)
#     a = a[:-1]
#
# print(a)
