from day_11 import Graph


def test_case_1():
    input = [4,
             [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]],
             [3, 2],
             [0, 3],
             [1, 3, 4],
             [0, 3]]
    expected = [None, 6, -1, None, 6]
    solution = Graph(input[0], input[1])
    assert solution.shortestPath(input[2][0], input[2][1]) == expected[1]
    assert solution.shortestPath(input[3][0], input[3][1]) == expected[2]
    solution.addEdge(input[4])
    assert solution.shortestPath(input[5][0], input[5][1]) == expected[4]
