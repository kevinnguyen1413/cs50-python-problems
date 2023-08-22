
import random
import sys

def main():
    guess()

while True:
    try:
        level = int(input('Level: '))
        random_number = random.randint(1, level)
    except ValueError:
        continue
    else:
        break

def guess():
    while True:
        try:
            guess = int(input(f'Guess a number between 1 and {level}: '))
        except ValueError:
            continue
        else:
            if guess not in range(1, level+1):
                continue
            elif guess < random_number:
                print('Too small!')
            elif guess > random_number:
                print('Too large!')
            else:
                print('Just right!')
                sys.exit()

main()