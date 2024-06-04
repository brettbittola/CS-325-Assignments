# Brett Bittola
# 2/5/2024
# CS 325
# Returns a set of non-sequential integers with the greatest sum


def max_independent_set(nums):
    """Determines the maximum sum of non-sequential numbers"""
    include = [0] * len(nums)
    included_set = []

    include[0] = max(0, nums[0])
    include[1] = max(include[0], nums[1])

    for i in range(2, len(nums)):
        if nums[i] > 0:
            include[i] = max(include[i - 1], include[i - 2] + max(0, nums[i]))

    i = len(nums) - 1
    while i >= 0:
        if i == 0 or include[i] != include[i - 1]:
            if nums[i] > 0:
                included_set.append(nums[i])
                i -= 2
            else:
                i -= 1
            if i < 0:
                break

        else:
            i -= 1

    return included_set


# adapted from https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
