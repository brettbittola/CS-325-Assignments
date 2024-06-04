def threes_and_fives(num):
    if num < 8:
        return "Please enter a number greater than or equal to 8."

    threes = 0
    fives = 0

    if num % 5 == 0:
        fives = num / 5
    elif num % 5 == 1:
        fives = (num - 6) / 5
        threes = 2
    elif num % 5 == 2:
        fives = (num - 12) / 5
        threes = 4
    elif num % 5 == 3:
        fives = (num - 3) / 5
        threes = 1
    else:
        fives = (num - 9) / 5
        threes = 3
    return int(threes), int(fives)
