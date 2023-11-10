# Count Number of Homogenous Substrings


# Intuition
My initial approach to solve this problem was to use regular expressions.
Regular expressions have a constant time complexity and means the `re.findall` built-in can be used with a linear time complexity to find all of the homogenous substrings.

# Approach
First of all I went to [regexr.com](https://regexr.com), a regular expression testing site, to come up with a regular expression to find all of the substrings. After looking at the cheatsheet I came up with `(.)\1+`. This matches any character then any more matching the first character of the substring. I tried running this in python and it was only returning the first character. To change it to be python compliant, I had to add `()` to the outside of the statement which resulted in `re.findall` returning tuples where 0 was the full result and 1 was the character. Using a list comprehension I was able to extract only the first value needed.

There is a formula to find how many homogenous substrings a substring contains. This is `s * (s+1) / 2` where `s` is the length of the substring.
Iterating through our substrings to calculate this value gives us the total.

As the total needs to be mod by `10^9 + 7`, we can just return the total mod `10^9 + 7` at the end resulting in a working solution.

After looking at some other solutions to see what methods other people had used I kept seeing `itertools.groupby` showing up and as such I did some research on it. Turns out this function does the exact same the regex part of my solution but without the added iteration of extracting the actual result. As such I used the for loop example from the documentation to adapt my code to use `itertools` instead of `re`. This shaved off about 40ms of total execution time.

# Complexity
- Time complexity:
The time complexity for both my solutions was $$O(n)$$ as the longer the length of the string (n) the longer the time to execute. Itertools was faster as it only had to iterate once over substrings as opposed to twice.



- Space complexity:
The space complexity for both of my solutions was $$O(n)$$ as they both depend on an array of substrings, the size of which is defined by the length of the string (n)
# Code
```py
class Solution:
    def countHomogenous(self, s: str) -> int:
        pattern = re.compile(r'((.)\2*)')
        homogenous_substrings = [x[0] for x in re.findall(pattern, s)]
        total = 0
        for substring in homogenous_substrings:
            total += len(substring) * (len(substring) + 1) // 2
        return total % (10**9 + 7)
```

```py
class Solution:
    def countHomogenous(self, s: str) -> int:
        total = 0
        for _, group in itertools.groupby(s):
            group_len = len(list(group))
            total += (group_len * (group_len + 1)) // 2
        return total % (10**9 + 7)
        
```
