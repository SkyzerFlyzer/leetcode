from day_7 import Solution

def test_case_1():
    dist = [1, 3, 4]
    speed = [1, 1, 1]
    value = Solution.eliminateMaximum(Solution, dist, speed)
    assert value == 3


def test_case_2():
    dist = [1, 1, 2, 3]
    speed = [1, 1, 1, 1]
    value = Solution.eliminateMaximum(Solution, dist, speed)
    assert value == 1

def test_case_3():
    dist = [3, 2, 4]
    speed = [5, 3, 2]
    value = Solution.eliminateMaximum(Solution, dist, speed)
    assert value == 1
