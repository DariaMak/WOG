from games.memory_game import play as memory_play
from games.currency_roulette_game import play as currency_roulette_play
from games.guess_game import play as guess_play
from score import add_score


def welcome():
    user_name = input(f"Write me your name please: \n")
    user_name = user_name.capitalize()
    print(f'Hi {user_name} and welcome to the World of Games: the Epic Journey')
    return


def game_result(result,level):
    if result:
        print('You win!')
        add_score(level)
    else:
        print('Sorry you lose')


def start_play():
    games = {"Memory Game": "a sequence of numbers will appear for 1 second and you have to guess it back.",
             "Guess Game": "guess a number and see if you chose like the computer.",
             "Currency Roulette": "try and guess the value of a random amount of USD in ILS"}
    options = ""
    counter = 1
    for game_name, game_description in games.items():
        options += f"{counter}. {game_name} - {game_description}\n"
        counter += 1

    while True:
        choice = input(f"Please select your game from the options [by number 1-3]: \n{options}")
        if choice.isdigit() and 1 <= int(choice) <= 3:
            choice = int(choice)
            break
        else:
            print("Invalid input. Please enter a number between 1 and 3.")

    while True:
        level = input(f"Please select your game level between 1-5 [1=low to 5=high]: \n")
        if level.isdigit() and 1 <= int(level) <= 5:
            level = int(level)
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

    if choice == 1:
        game_result(memory_play(level),level)
    elif choice == 2:
        game_result(guess_play(level),level)
    elif choice == 3:
        game_result(currency_roulette_play(level),level)
    return


