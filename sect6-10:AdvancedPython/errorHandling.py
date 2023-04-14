# # Error Handling
#
# while True:
#     try:
#         age = int(input('enter age  '))
#         10 / age
#     except ValueError:
#         print('please enter a number')
#     except ZeroDivisionError:
#         print('please enter an age greater than 0')
#     else:
#         print('thanks')
#         break

# # ----------------
#
# def sums(num1, num2):
#     try:
#         return num1 / num2
#     # except TypeError as err:
#     #     print(f'oops! {err}')
#     except (TypeError, ZeroDivisionError) as err:
#         print(f'oooooopsss!! {err}')
#
#
# print(sums(2, '4'))
# print(sums(4, 0))
#
# # ----------------

# while True:
#     try:
#         age = int(input('enter age  '))
#         10 / age
#     except ValueError:
#         print('please enter a number')
#         continue  # goes back to the top and runs again / still finally runs but print after finally DOES NOT
#     except ZeroDivisionError:
#         print('please enter an age greater than 0')
#         continue
#     else:
#         print('thanks')
#
#     # finally
#     finally:
#         print('FINALLY, I run regardless if it succeeded or not')
#
#     print('can you hear me')
#     break
#
# # ----------------

while True:
    try:
        age = int(input('enter age  '))
        10 / age
        # raise ValueError("cut it out")
        raise Exception("yo whatcha matcha")
    # except ValueError:
    #     print('please enter a number')
    #     continue  # goes back to the top and runs again / still finally runs but print after finally DOES NOT
    except ZeroDivisionError:
        print('please enter an age greater than 0')
        continue
    else:
        print('thanks')

    # finally
    finally:
        print('FINALLY, I run regardless if it succeeded or not')

    print('can you hear me')
    break
