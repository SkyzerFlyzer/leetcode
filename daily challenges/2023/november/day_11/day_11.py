import collections
from typing import List
import heapq

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.nodes = collections.defaultdict(dict)
        for edge in edges:
            self.nodes[edge[0]][edge[1]] = edge[2]

    def addEdge(self, edge: List[int]) -> None:
        self.nodes[edge[0]][edge[1]] = edge[2]

    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 == node2:
            return 0
        distances = collections.defaultdict(int)
        distances[node1] = 0
        queue = [(0, node1)]
        heapq.heapify(queue)
        while queue:
            distance, node = heapq.heappop(queue)
            if node == node2:
                break
            if distance > distances[node]:
                continue
            for neighbour, weight in self.nodes[node].items():
                if neighbour not in distances or distance + weight < distances[neighbour]:
                    distances[neighbour] = distance + weight
                    heapq.heappush(queue, (distance + weight, neighbour))
        if node2 not in distances:
            return -1
        return distances[node2]




# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
