def highest_even(li):
    number = []
    for item in li:
        if item % 2 == 0:
            number.append(item)
    return max(number)


# def highest_even(li):
#     num = 0
#     for rem in li:
#         if rems % 2 == 0:
#             if num is 0 or num

#     return li

print(highest_even([10,2,3,4,8,11]))