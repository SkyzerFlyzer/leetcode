class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        if not vowels.intersection(s):
            return s
        unordered_vowels = []
        vowel_indexes = []
        for x in range(len(s)):
            if s[x] in vowels:
                unordered_vowels.append(s[x])
                vowel_indexes.append(x)
        unordered_vowels.sort()
        if len(unordered_vowels) == len(s):
            return ''.join(unordered_vowels)
        ordered_string = []
        for x in range(len(s)):
            if x in vowel_indexes:
                ordered_string.append(unordered_vowels.pop(0))
                continue
            ordered_string.append(s[x])
        return ''.join(ordered_string)





