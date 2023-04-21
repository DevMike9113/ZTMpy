from random import randint


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('correctomundo')
            # break - is for loops
            return True
    else:
        print('hey 1-10 man')


if __name__ == '__main__':
    answer = randint(1, 10)
    while True:
        try:
            guess = int(input('type a number 1-10:  '))
            if run_guess(guess, answer):
                break
        except ValueError:
            print('please enter a number')
            continue
