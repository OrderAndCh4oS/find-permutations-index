import timeit
from math import factorial

"""
    Found from: https://stackoverflow.com/a/12147386/2562137
    Only works if all characters are distinct
"""
def lexicographic_index(p):
    """
    Return the lexicographic index of the permutation `p` among all
    permutations of its elements. `p` must be a sequence and all elements
    of `p` must be distinct.
    True
    """
    result = 1
    for j in range(len(p)):
        k = sum(1 for i in p[j + 1:] if i < p[j])
        result += k * factorial(len(p) - j - 1)
    return result

print(lexicographic_index('QUESTION'))

if __name__ == '__main__':
    print('Getting Benchmark...')
    print(timeit.timeit("lexicographic_index('QUESTION')", number=100, setup="from __main__ import lexicographic_index") / 100)
    print('Done.')
