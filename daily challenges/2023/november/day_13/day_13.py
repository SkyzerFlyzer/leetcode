import re
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_pattern = re.compile(r'[aeiouAEIOU]')
        if not re.search(vowels_pattern, s):
            return s
        vowels = []
        index = []
        for vowel in re.finditer(vowels_pattern, s):
            vowels.append(vowel.group())
            index.append(vowel.start())
        vowels.sort()
        if len(vowels) == len(s):
            return ''.join(vowels)
        ordered_string = ''
        prev = 0
        for i in index:
            ordered_string += s[prev:i]
            ordered_string += vowels.pop(0)
            prev = i+1
        ordered_string += s[prev:]
        return ordered_string





