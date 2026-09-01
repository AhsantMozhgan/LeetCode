# https://leetcode.com/problems/minimum-genetic-mutation

from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        # BFS Initialization
        # Store the current gene and the number of mutations used to reach that gene.
        queue = deque([(startGene, 0)])

        # Store genes that we have already visited.
        visited = {startGene}

        # BFS
        while queue:

            # Get the current gene and the number of mutations used to reach it.
            current_gene, mutations = queue.popleft()

            # Check Target
            # If the current gene is the target gene, we found the minimum number of mutations.
            if current_gene == endGene:
                return mutations

            # Check Every Gene In The Bank
            # Compare the current gene with every valid gene in bank.
            for next_gene in bank:

                # Count how many characters are different between the current gene and next gene.
                differences = 0

                for i in range(len(current_gene)):

                    if current_gene[i] != next_gene[i]:
                        differences += 1

                # Valid Mutation
                # A valid mutation changes exactly one character.
                if differences == 1:

                    # Only process this gene if we have not visited it.
                    if next_gene not in visited:

                        # Mark the gene as visited.
                        visited.add(next_gene)

                        # Add the gene to BFS.
                        # One mutation is needed to reach this gene.
                        queue.append((next_gene, mutations + 1))

        # No Valid Mutation Path
        # If BFS finishes without reaching endGene, no valid mutation sequence exists.
        return -1

# Example Usage:
if __name__ == "__main__":
    solution = Solution()
    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = ["AACCGGTA"]
    result = solution.minMutation(start, end, bank)
    print(result)  # Expected output: 1

    
# I model each valid gene as a node in an unweighted graph. Two genes are connected if they differ by exactly one character. 
# I use BFS because I need the minimum number of mutations. For each current gene, I compare it with every gene in the bank and count how many characters are different. 
# If exactly one character is different and the gene hasn't been visited, I add it to the queue with mutations plus one. 
# The first time I reach the target gene, I return the number of mutations.
