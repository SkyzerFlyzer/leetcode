import collections


class Solution:
    @staticmethod
    def sortVowels(s: str) -> str:
        vowels_set = set('aeiouAEIOU')
        count = collections.Counter(s)
        if not vowels_set.intersection(count):
            return s
        vowels = set()
        for char in count:
            if char in vowels_set:
                vowels.add(char)
                s = s.replace(char, "_")
        if len(vowels) == len(s):
            return ''.join(sorted(vowels))
        for vowel in sorted(vowels):
            s = s.replace("_", vowel, count[vowel])
        return s






