"""Test for game guess number.
"""

from game_v2 import predict_number 


def test_game(predict_function):
    """Game testing function. A function that returns a tuple containing
    the maximum number of retries predictions and a dictionary, where the
    key is a guessed number, the value is the amount trying to guess 
    the number.
    """
    
    dict_guess = {} # A dictionary to collect the number of guessing attempts.
    
    for i in range(1,101):
        dict_guess[i] = predict_function(i)
        
    return max(dict_guess.values()), dict_guess


if __name__ == '__main__':
    # Run
    print(test_game(predict_number))