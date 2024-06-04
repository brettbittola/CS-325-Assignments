# Brett Bittola
# 2/12/2024
# CS 325
# Returns number of dogs that can be fed, based on hunger level and size of biscuits

def feedDog(hunger_level, biscuit_size):
    result = []
    biscuits = sorted(biscuit_size, reverse=True)
    hunger = sorted(hunger_level, reverse=True)
    count = len(hunger_level)
    for i in range(count):
        for biscuit in biscuits:
            if hunger[i] <= biscuit:
                result.append(biscuit)
                biscuits.remove(biscuit)
                break

    return len(result)


# adapted from activity selection exercise in module 5.3
