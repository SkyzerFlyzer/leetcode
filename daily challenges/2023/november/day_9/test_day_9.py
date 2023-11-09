from day_9 import Solution

def test_case_1():
    assert Solution().countHomogenous("abbcccaa") == 13

def test_case_2():
    assert Solution().countHomogenous("xy") == 2

def test_case_3():
    assert Solution().countHomogenous("zzzzz") == 15