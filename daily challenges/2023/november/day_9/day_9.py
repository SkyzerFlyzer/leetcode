import itertools
import re


class Solution:
    def countHomogenous(self, s: str) -> int:
        homogenous_substrings = itertools.groupby(s)
        total = 0
        for _, group in homogenous_substrings:
            group_len = len(list(group))
            total += (group_len * (group_len + 1)) // 2
        return total % (10**9 + 7)