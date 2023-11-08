class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x_travel = abs(sx - fx)
        y_travel = abs(sy - fy)
        total_travel = max(x_travel, y_travel)
        if total_travel > t:
            return False
        if total_travel == 0 and t == 1:
            return False
        return True
