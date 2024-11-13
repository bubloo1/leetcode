"""
# Definition for a Node."""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visitedNodes = {}

        def dfs(node):
            if node in visitedNodes:
                return visitedNodes[node]
            copy = Node(node.val)
            visitedNodes[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node) if node else None
    
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Step 2: Assign neighbors based on the adjacency list
node1.neighbors = [node2, node4]  # Neighbors of node 1 are 2 and 4
node2.neighbors = [node1, node3]  # Neighbors of node 2 are 1 and 3
node3.neighbors = [node2, node4]  # Neighbors of node 3 are 2 and 4
node4.neighbors = [node1, node3]  # Neighbors of node 4 are 1 and 3

newObject = Solution()
print(newObject.cloneGraph(node1))