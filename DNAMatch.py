# Brett Bittola
# 1/30/2024
# CS 325
# Dynamic Programming Top-Down and Bottom-Up Approach to Longest Common Subsequence


def dna_match_topdown(DNA1, DNA2, m=None, n=None, cache=None):
    """Recursive top-down approach to finding the longest common subsequence of two strings of DNA"""
    if m is None:
        m = len(DNA1)
    if n is None:
        n = len(DNA2)
    if cache is None:
        cache = {}

    if (m, n) in cache:
        return cache[(m, n)]

    if m == 0 or n == 0:
        return 0

    if DNA1[m - 1] == DNA2[n - 1]:
        answer = 1 + dna_match_topdown(DNA1, DNA2, m - 1, n - 1, cache)
    else:
        answer = max(dna_match_topdown(DNA1, DNA2, m - 1, n, cache), dna_match_topdown(DNA1, DNA2, m, n - 1, cache))

    cache[(m, n)] = answer
    return answer


def dna_match_bottomup(DNA1, DNA2, i=None, j=None):
    """Bottom-up approach to finding the longest common subsequence of two strings of DNA"""
    if i is None:
        i = len(DNA1)
    if j is None:
        j = len(DNA2)

    if i == 0 or j == 0:
        return 0

    cache = [[0 for x in range(j+1)] for x in range(i+1)]

    for m in range(i+1):
        for n in range(j+1):
            if m == 0 or n == 0:
                cache[m][n] = 0
            elif DNA1[m-1] == DNA2[n-1]:
                cache[m][n] = cache[m-1][n-1] + 1
            else:
                cache[m][n] = max(cache[m-1][n], cache[m][n-1])
    return cache[i][j]
