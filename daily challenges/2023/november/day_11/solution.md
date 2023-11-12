# Intuition
Immediately on viewing the problem my instinct was to go with a python implementation of Dijkstra's algorithm which allows you to find the shortest path between two nodes. As such I would need a map telling me where each node can go so that I could quickly access the data I needed.

# Approach
When initializing the object the number of nodes as well as the edges are passed in. However, the number of nodes doesn't actually matter as if there is no path between nodes then you simply return a -1. Using a `defaultdict` I was able to simply add each edge to its own key as the same edge can't appear twice. This also meant if a node is requested from the dict, and it doesn't exist it will return no edges, making this storage extremely efficient.

To add an edge all I had to do was simply assign the node's edge dictionary key. 

Implementing the shortest path was the most complex.
Originally, to store the nodes that need to be visited I used a normal queue and then iterated over it until it was empty, keeping track of the smallest distance to each node in another `defaultdict` and adding the edges to the queue.
This got me my first working solution but this was slow. As such I went back to the algorithm and realised I should be using a priority queue instead of a normal queue.
Using `heapq`, I was able to implement a heap to store the nodes that needed to be visited.
This allowed me to visit the paths in distance order, drastically improving search speed.

# Complexity
- Time complexity:
Class initialization has an $$O(E)$$ time complexity where `E` is the number of edges.<br>Adding an edge has an $$O(1)$$ time complexity.<br>Calculating the shortest path has an $$O((V + E) * log(V))$$ time complexity where `V` is the total nodes with edges and `E` is the number of edges

- Space complexity:
All large data structures have an $$O(V + E)$$ where `V` is the total nodes with edges and `E` is the number of edges.

# Code
```py
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
```