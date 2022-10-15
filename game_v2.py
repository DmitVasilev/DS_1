"""Game guess number.
the computer guesses the given number
"""

import numpy as np

def random_predict(number:int = 1) -> int:
    """Random predict number

    Args:
        number (int, optional): Given number. Defaults to 1.

    Returns:
        int: count of tries
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # estimated number
        if number == predict_number:
            break # out of cycle, if guessed
    return(count)
        
# print(f"Count of tries: {random_predict()}")


def score_game(random_predict) -> int:
    """How many tries on average in 1000 tries gusses our algorithm
    
    Args:
        random_predict (_type_): function guessin

    Returns:
        int: averege number of tries
    """
    
    count_ls = [] # list for saving number of tries
    np.random.seed(1) # fixed seed for replay
    # made a list of number
    random_array = np.random.randint(1, 101, size=(1000)) 
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls)) # find average number of tries
    
    print(f"Your algorithm guesses the number on average in: {score} tries")
    return(score)

if __name__ == '__main__':
    # Run
    score_game(random_predict)