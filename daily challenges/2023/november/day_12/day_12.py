from typing import List
import heapq


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        buses = {}
        for x in range(len(routes)):
            buses[x] = set(routes[x])
        queue = []
        for stops in buses.values():
            if source in stops:
                queue.append((1, stops))
        seen = set()
        while queue:
            distance, bus_stops = queue.pop(0)
            if target in bus_stops:
                return distance
            for x in range(len(routes)):
                if x not in seen and bus_stops.intersection(buses[x]):
                    seen.add(x)
                    queue.append((distance + 1, buses[x] - seen))
        return -1

