# https://leetcode.com/problems/clone-graph

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:  # Step 1: Handle edge case for empty graph
            return None

        # A dictionary to keep track of cloned nodes.
        clones = {}

        # Step 2: Define the DFS function to clone the graph
        def dfs(n):
            if n in clones:  # Check if we have already cloned this node
                return clones[n]
            
            # Clone the node
            clone_node = Node(n.val)
            clones[n] = clone_node  # Store the clone in the dictionary
            
            # Clone all the neighbors
            for neighbor in n.neighbors:
                clone_node.neighbors.append(dfs(neighbor))  # Recur for neighbors
            
            return clone_node

        # Step 3: Start cloning the graph using DFS from the given node
        return dfs(node)

# Example Usage
if __name__ == "__main__":
    # Create a simple graph
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    node1.neighbors = [node2, node4]  # Node 1 is connected to Node 2 and Node 4
    node2.neighbors = [node1, node3]   # Node 2 is connected to Node 1 and Node 3
    node3.neighbors = [node2]          # Node 3 is connected to Node 2
    node4.neighbors = [node1, node3]   # Node 4 is connected to Node 1 and Node 3

    solution = Solution()
    cloned_graph = solution.cloneGraph(node1)

    # Function to print the graph (for verification)
    def print_graph(node):
        visited = set()
        def dfs_print(n):
            if n in visited:
                return
            visited.add(n)
            print(f'Node {n.val} with neighbors: {[neighbor.val for neighbor in n.neighbors]}')
            for neighbor in n.neighbors:
                dfs_print(neighbor)
        
        dfs_print(node)

    print("Original Graph:")
    print_graph(node1)

    print("\nCloned Graph:")
    print_graph(cloned_graph)


# I use DFS to traverse the graph and a HashMap to map each original node to its cloned node. When I visit a node for the first time, I create its clone and immediately store it in the HashMap before processing its neighbors. 
# Then I recursively clone each neighbor and add the cloned neighbor to the current clone's neighbor list. 
# If I encounter a node that is already in the HashMap, I return its existing clone. This handles cycles and ensures that every original node is cloned exactly once.
