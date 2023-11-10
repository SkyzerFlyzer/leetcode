from day_10 import Solution


def test_case_1():
    data = [[2, 1], [3, 4], [3, 2]]
    expected = [1, 2, 3, 4].sort()
    solution = Solution()
    assert solution.restoreArray(data).sort() == expected


def test_case_2():
    data = [[4, -10], [-1, 3], [4, -3], [-3, 3]]
    expected = [-10, 4, -3, 3, -1].sort()
    solution = Solution()
    assert solution.restoreArray(data).sort() == expected
