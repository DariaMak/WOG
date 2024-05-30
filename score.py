from utils import SCORES_FILE_NAME


def add_score(difficulty):
    global POINTS_OF_WINNING
    POINTS_OF_WINNING = (difficulty * 3) + 5
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            data = file.read()
            POINTS_OF_WINNING += int(data)
    except FileNotFoundError:
        with open(SCORES_FILE_NAME,'w') as file:
            file.write('0')

    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(POINTS_OF_WINNING))

    return