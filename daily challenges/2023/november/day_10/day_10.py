import itertools
import collections
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
        sorted_graph = sorted(graph.items(), key=lambda x: len(x[1]))
        start, _ = sorted_graph[0]
        end, _ = sorted_graph[1]
        seen = {start}
        num = []
        num.append(start)
        while num[-1] != end:
            potential = graph[num[-1]]
            for neighbour in potential:
                if neighbour not in seen:
                    seen.add(neighbour)
                    num.append(neighbour)
                    break
        return num












