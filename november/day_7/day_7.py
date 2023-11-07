from typing import List

class Solution:

    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        monsters = list(sorted(map(list, zip(dist, speed)), key=lambda x: x[0]/x[1]))
        kills = 0
        while monsters[0][0] > 0:
            kills += 1
            monsters.pop(0)
            if not monsters:
                break
            monsters[0][0] -= kills * monsters[0][1]
        return kills



if __name__ == '__main__':
    print(Solution.eliminateMaximum(Solution, [1, 3, 4], [1, 4, 1]))