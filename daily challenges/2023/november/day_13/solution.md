# Intuition
My initial thoughts on how to solve this problem was to check each character, if it was a vowel replace it with a vowel from a list that was already sorted and continue.

# Approach
My intuition turned out to be hard to implement and as a result I decided to replace all vowels with a placeholder and keep track of how many of each vowel there was. That way I would be able to sort the unique vowels and replace the placeholder the amount of times that vowel appears.

To do this I originally iterated over the string twice, but this was slow as I was also rebuilding the string and popping from a list of vowels.

I then attempted a regex solution which was faster but, I was still in the lower 50% of submissions, so I knew there must be a better implementation than what I was doing.

After a little research I came across the counter class from the `collections` library. This allowed me to quickly count how many of each vowel there was in the string. Adapting my previous code's optimisations to work with the new method of replacing x amount of vowels at a time meant that I could drastically improve speeds as I would have to do a lot less iterations.

# Complexity
- Time complexity:
The time complexity of the algorithm is $$O(n + k log(k)) $$ where `k` is the number of unique vowels.

- Space complexity:
The space complexity of the algorithm is $$O(n)$$ as everything is dependent on the length of the inputted string.

# Code
```py
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
```