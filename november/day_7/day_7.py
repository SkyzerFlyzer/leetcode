import heapq
import math
from typing import List

class Solution:

    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        monsters = [i[0]/i[1] for i in zip(dist, speed)]
        heapq.heapify(monsters)
        print(monsters)
        kills = 0
        while True:
            if not monsters:
                return kills
            if math.ceil(heapq.heappop(monsters)) > kills:
                kills += 1
                continue
            return kills



if __name__ == '__main__':
    print(Solution.eliminateMaximum(Solution, [1, 3, 4], [1, 4, 1]))