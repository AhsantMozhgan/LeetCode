# https://leetcode.com/problems/evaluate-division

from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        # Step 1: Build the graph
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend].append((divisor, value))  # Edge from dividend to divisor
            graph[divisor].append((dividend, 1 / value))  # Edge from divisor to dividend

        def dfs(src: str, dst: str, visited: set) -> float:
            if src == dst:
                return 1.0  # If both are the same, the result is 1
            visited.add(src)
            for neighbor, value in graph[src]:
                if neighbor in visited:
                    continue
                result = dfs(neighbor, dst, visited)
                if result != -1.0:
                    return result * value  # Multiply the weight of the edge
            return -1.0  # Return -1 if no path found

        results = []
        # Step 2: Evaluate each query
        for dividend, divisor in queries:
            if dividend in graph and divisor in graph:
                results.append(dfs(dividend, divisor, set()))  # Perform DFS for the current query
            else:
                results.append(-1.0)  # If either node is not in the graph, answer is -1

        return results

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "y"]]
    results = solution.calcEquation(equations, values, queries)
    print(results)  # Expected Output: [6.0, 0.5, -1.0, 1.0, -1.0]

# I model each equation as a weighted graph. For an equation like a divided by b equals 2, I create an edge from a to b with weight 2, and a reverse edge from b to a with weight 0.5. 
# Then for each query, I use DFS to find a path from the dividend to the divisor. When I reach the destination, I return 1, and as the recursion unwinds, I multiply the edge weights along the path. 
# I also use a visited set to avoid cycles. If either variable doesn't exist or there is no path, I return -1.
# Why do you use a graph? Because each equation represents a relationship between two variables, and the value of that relationship can be represented as an edge weight.
