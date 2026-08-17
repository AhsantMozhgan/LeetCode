# https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         # Create a set for quick lookup
        number_set = set(nums)

        # Track Longest Sequence. longest_sequence stores the longest consecutive sequence found so far.
        longest_sequence = 0

        # Check Every Number. Try each number as a possible beginning of a consecutive sequence.
        for number in number_set:

            # Check if it is the start of a sequence
            # A number is the START of a consecutive sequence only if number - 1 does not exist.
            if number - 1 not in number_set:

                # Count consecutive numbers
                # We found the beginning of a consecutive sequence. Start counting from this number.
                current_number = number
                current_length = 1

                # Continue while the next consecutive number exists.
                while current_number + 1 in number_set:
                    current_number += 1
                    current_length += 1

                # Compare the current sequence with the longest sequence found so far.
                longest_sequence = max(longest_sequence, current_length)

        # Return the longest consecutive sequence length.
        return longest_sequence

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test case
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4


# The brute-force way would be to sort the array and then count consecutive numbers, but sorting costs O(n log n).  

# To do it in linear time, I first put every number into a hash set. That gives me O(1) lookups and also removes duplicates automatically.  

# Then I iterate through every number in the set. I only start counting a sequence when the current number is the beginning of one — that is, when number − 1 is **not** in the set.  

# For example, if I see 3 and 2 is also present, then 3 is somewhere in the middle of a sequence, so I skip it. But if I see 1 and 0 is missing, then 1 is a true starting point.  

# Once I find a starting number, I keep checking whether the next consecutive number exists (current + 1), advancing and counting the length until the sequence ends. 
# After each sequence I update the global maximum length.  

# The key optimization is that I only expand sequences from their actual starts. That way every number is examined at most a constant number of times, keeping the whole algorithm O(n).
  