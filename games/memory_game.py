import random
import os
from time import sleep
from utils import Screen_cleaner


def generate_sequence(level):
    random_list = [random.randint(1, 101) for __ in range(level)]
    return random_list


def get_list_from_user(random_list: list):
    while True:
        input_str = input(f'\rPlease enter {len(random_list)} number/s as a list, separated by comma: ')
        input_values = input_str.split(',')

        try:
            input_list = [int(val.strip()) for val in input_values]
            if len(input_list) != len(random_list):
                raise ValueError("Number of elements does not match")
            break
        except ValueError:
            print("Invalid input. Please enter integers separated by commas.")
    return input_list


def is_list_equal(random_list,input_list):
    random_list.sort()
    input_list.sort()
    return True if random_list == input_list else False


def play(level):
    random_list = generate_sequence(level)
    for _ in range(5):
        sleep(2)
        print(f'\r {random_list}', end='\r')
        sleep(2)
        Screen_cleaner()  # Clear the screen
    input_list = get_list_from_user(random_list)
    return is_list_equal(random_list,input_list)


# print(play(2))



