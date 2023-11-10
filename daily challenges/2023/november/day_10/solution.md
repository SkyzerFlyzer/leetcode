# Restore the Array From Adjacent Pairs
## Intuition
My initial thought to solve this problem was to use a linked list to link pairs together. That way I would be able to create the list by iterating through the linked list. The start and end values would only appear once in adjacent pairs whereas the middle values would appear twice. This would give me a easy way to find the start and the end values.

## Approach
When aproaching the problem I had to initially do some research to see if python supported linked lists. Unfortunately a custom class needed to be implemented to support them and as such I opted to not use them as the challenge should be abble to be completed without adding custom objects.

Whilst researching the linked list idea I came up with the idea to implement it as a map instead. That way I would be able to simply access the next key through the value of the first. This approach worked for most test cases, however there was a small flaw in the logic that meant that if the start and end values were the wrong way around, it would miss an adjacent pair.

Finally, I decided to map potential nodes for each node using a dictionary. This allowed me to figure out where I could go next and using a set, I was able to keep track of nodes I had previously visited. Sorting the values by the length of the array, I was able to find the start and end values. Then I simply iterated through the dictionary until I reached the end value, adding to a list on each iteration. This resulted in generating the original number array

## Complexity
- Time complexity:
The overall time complexity is dominated by the sorting of the graph and can be expressed as $$O(n + V log V)$$, where `n` is the number of adjacent pairs and `V` is the number of nodes.

- Space complexity:
The space required to store the graph using a dictionary can take up to $$O(n + m)$$ space, where n is the number of nodes and m is the number of edges.<br>The seen set and num list take up an $$O(n)$$ space complexity as these are dependent on the number of adjacent pairs.<br>Therefore the overall space complexity is $$O(n+ m)$$.


## Code
```
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
```