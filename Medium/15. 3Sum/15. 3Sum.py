# https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicate numbers for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Since array is sorted, no possible triplet
            if nums[i] > 0:
                break

            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second and third elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:  # current_sum > 0
                    right -= 1
        
        return result

# I’d first sort the array. Sorting lets me use the two-pointer technique and makes it straightforward to skip duplicate triplets.  

# Then I iterate through the array, treating each number as the first element of a potential triplet. For a fixed `nums[i]`,
# I place a left pointer right after `i` and a right pointer at the end of the array, looking for two values that sum to `-nums[i]`.  

# - If the current sum is too small, I move left right to increase it.  
# - If the sum is too large, I move right left to decrease it.  
# - When the sum is zero, I record the triplet and skip any duplicate values at both pointers so I never add the same triplet twice.  

# I also skip duplicates for the first number itself. And once `nums[i]` becomes positive I can stop early, 
# because the remaining sorted values are also positive and no triplet can sum to zero.  

# Sorting costs O(n log n) and the nested two-pointer work is O(n²), so the overall time complexity is O(n²). 
# Extra space is O(1) if we ignore the output and the sorting implementation.