from day_13 import Solution


def test_case_1():
    s = "lEetcOde"
    solution = Solution()
    assert solution.sortVowels(s) == "lEOtcede"
