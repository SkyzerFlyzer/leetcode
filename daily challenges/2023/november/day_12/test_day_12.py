from day_12 import Solution

def test_case_1():
    routes = [[1,2,7],[3,6,7]]
    source = 1
    target = 6
    expected = 2
    solution = Solution()
    assert solution.numBusesToDestination(routes, source, target) == expected

def test_case_2():
    routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
    source = 15
    target = 12
    expected = -1
    solution = Solution()
    assert solution.numBusesToDestination(routes, source, target) == expected

def test_case_3():
    routes = [[1,7],[3,5]]
    source = 5
    target = 5
    expected = 0
    solution = Solution()
    assert solution.numBusesToDestination(routes, source, target) == expected