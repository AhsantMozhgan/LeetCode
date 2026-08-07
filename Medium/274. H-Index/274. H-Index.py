# https://leetcode.com/problems/h-index

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse=True)  # Sort the citations in descending order

        h = 0  # Initialize H-Index

        # Iterate through the sorted citations
        for i in range(len(citations)):
            if citations[i] >= i + 1:  # Check if at least `i + 1` papers have `citations[i]` or more
                h = i + 1  # Update H-Index
            else:
                break  # No need to continue if the condition is not met

        return h  # Return the calculated H-Index


# The h-index is the largest number h such that there are at least h papers with at least h citations each.  

# I first sort the citation counts in descending order so the most-cited papers come first.  

# Then I scan the sorted array. At index i I check whether `citations[i]` is at least `i + 1`.  
# If it is, the first `i + 1` papers all have at least `i + 1` citations, so `i + 1` is a valid h-index and I keep it.  
# As soon as the condition fails I can stop, because every remaining citation count is smaller and no larger h can be valid.  

# The final value I kept is the largest valid h-index.  

# Sorting makes the solution O(n log n) time, and it uses only constant extra space beyond the sort itself.