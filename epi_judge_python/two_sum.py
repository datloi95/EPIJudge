from typing import List

from test_framework import generic_test


def has_two_sum(A: List[int], t: int) -> bool:
    hash_set = set()
    for num in A:
        hash_set.add(num)
    for num in A:
        if (t-num) in hash_set:
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sum.py', 'two_sum.tsv',
                                       has_two_sum))
