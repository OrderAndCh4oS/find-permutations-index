import itertools
import timeit

def find_permutation_index(word):
    """Return the anagram list position of the word"""
    n = len(word)
    if not n:
        return False
    initial_word = list(word)
    word = sorted(word)

    count = 1
    while not sorted(word)[::-1] == word:
        i = 0
        for i in range(n - 1, 0, -1):
            if word[i - 1] < word[i]:
                break

        x = word[i - 1]
        smallest = i
        for j in range(i + 1, n):
            if word[j] > x and word[j] < word[smallest]:
                smallest = j

        word[smallest], word[i - 1] = word[i - 1], word[smallest]
        word = word[:i] + sorted(word[i:])
        count += 1
        if word == initial_word:
            break

    return count

def find_permutation_index_two(word):
    return sorted(list(set(''.join(item) for item in itertools.permutations(word)))).index(word) + 1

print(find_permutation_index('QUESTION'))
print(find_permutation_index('QUESTIONER'))
print(find_permutation_index('BOOKKEEPER'))
print(find_permutation_index_two('QUESTION'))
print(find_permutation_index_two('QUESTIONER'))
print(find_permutation_index_two('BOOKKEEPER'))

if __name__ == '__main__':
    print('Getting Benchmarks...')
    print(timeit.timeit("find_permutation_index('QUESTIONER')", number=10, setup="from __main__ import find_permutation_index") / 10)
    print(timeit.timeit("find_permutation_index_two('QUESTIONER')", number=10, setup="from __main__ import find_permutation_index_two") / 10)
    print('Done.')
