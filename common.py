""" Common module
implement commonly used functions here
"""

import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''

        generated = ''

    lower_let = 'qwertyuioplkjhgfdsazxcvbnm'
    upper_let = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
    digit = '1234567890'
    special = '!@#$%^&*'
    

    for i in range(2):
        generated += random.choice(lower_let)
        generated += random.choice(upper_let)


    for i in range(2):
        generated += random.choice(digit)


    for i in range(2):
        generated += random.choice(special)

    

    for i in range(1):
        for row in table:
            if (str(row[0])) ==  generated:
                generate_random(table)



    return generated
