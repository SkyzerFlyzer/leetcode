import re


class Solution:
    def countHomogenous(self, s: str) -> int:
        pattern = re.compile(r'((.)\2*)')
        homogenous_substrings = [x[0] for x in re.findall(pattern, s)]
        total = 0
        for substring in homogenous_substrings:
            total += len(substring) * (len(substring) + 1) // 2
        return total % (10**9 + 7)