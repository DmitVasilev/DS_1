"""Game guess number.

The computer guesses the given number.

"""

import numpy as np


def predict_number(number:int = 1) -> int:
    """Predict number

    Args:
        number (int, optional): Given number. Defaults to 1.

    Returns:
        int: count of tries

    """

    count = 0  # Number of tries
    number_max = 101  # Maximum limit of the guess range
    number_min = 1  # Minimum limit of the guess range

    while True:
        count += 1
        predict_number = (number_min+number_max) // 2

        if number > predict_number:
            number_min = predict_number

        elif number < predict_number:
            number_max = predict_number

        else:            
            break  # Out of cycle, if guessed

    return(count)


def score_game(predict_function) -> int:
    """How many tries on average in 1000 tries gusses our algorithm

    Args:
        random_predict (_type_): function guessin

    Returns:
        int: averege number of tries

    """

    count_ls = []  # List for saving number of tries
    np.random.seed(1)  # Fixed seed for replay
    # Made a list of number
    random_array = np.random.randint(1, 101, size = (1000))

    for number in random_array:
        count_ls.append(predict_function(number))
    score = int(np.mean(count_ls))  # Find average number of tries

    print(f"Your algorithm guesses the number on average in: {score} tries")
    return(score)


if __name__ == '__main__':
    # Run
    score_game(predict_number)
