from forex_python.converter import CurrencyRates
import random


def get_money_interval(level):
    c = CurrencyRates()
    converter = c.get_rate('USD', 'ILS')
    usd_number = random.randint(0, 100)
    ils_number = usd_number * converter
    interval_ils = 10 - level
    start = round(ils_number - interval_ils / 2, 0)
    stop = round(ils_number + interval_ils / 2, 0)
    money_interval = [start, stop]
    return money_interval


def get_guess_from_user(level):
    usd_amount = round(sum(get_money_interval(level))/2,0)
    while True:
        try:
            ils_guess = int(input(f"Please guess the amount in ILS of {usd_amount} USD: "))
            break
        except ValueError:
            print("Please enter a valid integer.")
    return ils_guess


def compare_results(level):
    user_guess = get_guess_from_user(level)
    interval = get_money_interval(level)
    if interval[0] <= user_guess <= interval[1]:
        return True
    else:
        return False


def play(level):
    run = compare_results(level)
    return run


# print(get_money_interval(2))