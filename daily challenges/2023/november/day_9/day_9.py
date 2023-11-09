import itertools
import re


class Solution:
    def countHomogenous(self, s: str) -> int:
        total = 0
        for _, group in itertools.groupby(s):
            group_len = len(list(group))
            total += (group_len * (group_len + 1)) // 2
        return total % (10**9 + 7)