# Brett Bittola
# 2/5/24
# Provides a power set of all possible combinations of a given set.

def powerset_helper(pointer, choices_made, inputset, result):
    if pointer < 0:
        result.append(choices_made[:])
        return

    choices_made.append(inputset[pointer])
    powerset_helper(pointer-1, choices_made, inputset, result)
    choices_made.pop()
    powerset_helper(pointer-1, choices_made, inputset, result)


def powerset(inputset):
    result = []
    powerset_helper(len(inputset)-1, [], inputset, result)
    return result


# Code adapted from the pseudocode for the exercise at the end of module 4.4
