import random


def generate_number(level):
    secret_number = random.randint(1, level*10)
    return secret_number


def get_guess_from_user(level):
    guess = int(input(f"Please guess number [by number 1-{level*10}]: \n"))
    return guess


def compare_results(random_num,guess_num):
    if random_num == guess_num:
        return True
    else:
        return False


def play(level):
    random_num = generate_number(level)
    guess_num = get_guess_from_user(level)
    return compare_results(random_num, guess_num)