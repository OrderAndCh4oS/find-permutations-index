import collections
import timeit
from math import factorial


def count_permutations(word):
    repeat_counts = collections.Counter(word)
    x = factorial(len(word))
    for v in repeat_counts.values():
        x /= factorial(v)
    return x

print(count_permutations('BOOKKEEPER'))

if __name__ == '__main__':
    print('Getting Benchmark...')
    print(timeit.timeit("count_permutations('BOOKKEEPER')", number=100, setup="from __main__ import count_permutations") / 100)
    print('Done.')