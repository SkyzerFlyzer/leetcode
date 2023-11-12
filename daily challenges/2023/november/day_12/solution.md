# Intuition
My initial thoughts to solving this problem was to use a modified version of dijkstra's algorithm. This way the shortest amount of buses can be found quickly and efficiently.

# Approach
After yesterday's challenge creating a basic dijkstra's algorithm in python was pretty simple. However instead of using nodes to edges where the edges are potential nodes to visit, nodes were instead buses and the edges were stops. This meant that an extract lookup was needed to confirm that the current bus stops at a stop within the potential bus' path. Obviously, we don't need to be getting on the same bus twice so each time a new bus is boarded, we add it to a seen set preventing it from being checked again. 

To implement the modified version of dijkstra's algorithm I utilised a dictionary of sets where the key was the bus and the set was the potential stops. As the time spent on the bus doesn't matter a simple intersection can be performed on the set to confirm that the bus shares stops with another bus. Additionally, this means that if the target is in the current set, the distance value can just be returned as there will only ever be more bus changes after the first bus contains the target stop.

# Complexity
- Time complexity:
The time complexity of this solution is $$O(N * M) $$ where `N` is the number of buses and `M` is the average number of stops.


- Space complexity:
The space complexity of this solution is $$O(N * M) $$ where `N` is the number of buses and `M` is the average number of stops.

# Code
```py
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
                    queue.append((distance + 1, buses[x]))
        return -1
        
```