"""Game predict number.
"""

import numpy as np

number = np.random.randint(1,101) # Guessing number

count = 0

while True:
    count += 1
    predict_number = int(input('Guess number from 1 to 100: '))
    
    if predict_number > number:
        print('Number must be lower!')
    
    elif predict_number < number:
        print('Number must be higer!')
    
    else:
        print(f'You gussed the number in {count} tries')
        break # End game, out of cycle
