import re


class Solution:
    def countHomogenous(self, s: str) -> int:
        homogenous_substrings = [x[0] for x in re.findall(r'((.)\2*)', s)]
        total = 0
        for substring in homogenous_substrings:
            total += len(substring) * (len(substring) + 1) // 2
        return total % (10**9 + 7)