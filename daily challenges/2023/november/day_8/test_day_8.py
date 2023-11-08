from day_8 import Solution


def test_case_1():
    sx = 2
    sy = 4
    fx = 7
    fy = 6
    t = 6
    assert Solution.isReachableAtTime(Solution, sx, sy, fx, fy, t)


def test_case_2():
    sx = 3
    sy = 1
    fx = 7
    fy = 3
    t = 3
    assert not Solution.isReachableAtTime(Solution, sx, sy, fx, fy, t)


def test_case_3():
    sx = 1
    sy = 2
    fx = 1
    fy = 2
    t = 1
    assert not Solution.isReachableAtTime(Solution, sx, sy, fx, fy, t)


def test_case_4():
    sx = 1
    sy = 1
    fx = 1
    fy = 1
    t = 3
    assert Solution.isReachableAtTime(Solution, sx, sy, fx, fy, t)
