# https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Voting Algorithm
        # Time: O(n)
        # Space: O(1)
        majority_candidate = None
        count = 0

        for num in nums:
            if count == 0:
                majority_candidate = num
            
            if num == majority_candidate:
                count += 1
            else:
                count -= 1

        return majority_candidate


# “I’d use the Boyer-Moore Voting Algorithm.  

# The idea is to keep a current candidate and a count that represents its net support.  

# As I go through the array, whenever the count drops to zero I pick the current number as the new candidate.  
# If the number matches the candidate I increment the count; if it doesn’t, I decrement it.  

# You can think of a matching number as giving the candidate one vote and any other number as canceling one of its votes.  
# Because the majority element appears more than half the time, it can never be completely canceled out by the rest of 
# the numbers, so it ends up as the final candidate.  

# The whole process runs in O(n) time and uses only O(1) extra space.

# ---

# Hash Map Algorithm:
# Time: O(n)
# Space: O(n)
# class Solution:
#     def majorityElement(self, nums):
#         majority_count = (len(nums) // 2

#         count = Counter(nums)
        
#         for key, val in count.items():
#             if val > majority_count:
#                 return key
