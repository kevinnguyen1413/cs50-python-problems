"""In a file called professor.py, implement a program that:

Prompts the user for a level, 
. If the user does not input 1, 2, or 3, the program should prompt again. X
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 
 digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again,
allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries,
the program should output the correct answer.
The program should ultimately output the user's score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and 
generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:"""


import random


def main():
    level = get_level()
    x, y = generate_integer(level)
    attempts(x, y)



def get_level():
    while True:
        try:
            chosen_level = int(input('Level: '))
        except ValueError:
            continue
        if chosen_level not in range(1,4):
            continue
        else:
            return chosen_level
        

def generate_integer(level):
    if level == 1:
        x, y = (random.randint(0, 9) for i in range(2))
        return x, y
    elif level == 2:
        x, y = (random.randint(10, 99) for i in range(2))
        return x, y
    else:
        x, y = (random.randint(100, 999) for i in range(2))
        return x, y


def attempts(x, y):
    attempts_allowed = 3
    score = 0
    while attempts_allowed > 0:
        try:
            answer = int(input(f'{x} + {y} = '))
        except ValueError:
            continue
        except EOFError:
            print('End Input')
        if answer != x + y:
            print('EEE')
            attempts_allowed -= 1
            continue
        elif answer == x + y and attempts_allowed == 3:
            score += 1
            generate_integer(chosen_level)
        else:
            break
    
    """print(f'Score: {score}')"""
        
        
    

    


if __name__ == "__main__":
    main()