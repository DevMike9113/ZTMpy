import sys
from random import randint

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        guess = int(input('type a number 1-10:  '))
        if 0 < guess < 11:
            if guess == answer:
                print('correctomundo')
                break
        else:
            print('hey 1-10 man')
    except ValueError:
        print('please enter a number')
        continue
