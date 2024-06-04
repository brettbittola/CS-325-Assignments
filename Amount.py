# Brett Bittola
# 2/12/2024
# CS 325
# Returns a combination of numbers in a set that, when added together, equal the target number

def amount_helper(amount_values, start, answer, remainder, combination):
    if remainder == 0:
        if combination not in answer:
            answer.append(combination[:])
        return
    elif remainder < 0:
        return
    for i in range(start, len(amount_values)):
        combination.append(amount_values[i])
        amount_helper(amount_values, i+1, answer, remainder-amount_values[i], combination)
        combination.pop()


def amount(amount_values, target_sum):
    answer = []
    amount_helper(amount_values, 0, answer, target_sum, [])
    return answer

# adapted from example code in the example of module 5.2
