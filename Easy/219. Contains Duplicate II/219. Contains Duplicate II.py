# https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        number_to_index = dict()  # To store the last seen index of each number
        
        for current_index, current_number in enumerate(nums):
            if current_number in number_to_index:
                # Check the difference between indices
                if current_index - number_to_index[current_number] <= k:
                    return True
            # Update the last seen index for the current number
            number_to_index[current_number] = current_index
        
        return False  # If no duplicates are found within k distance

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.containsNearbyDuplicate([1,2,3,1], 3))  # Output: True
    print(solution.containsNearbyDuplicate([1,0,1,1], 1))  # Output: True
    print(solution.containsNearbyDuplicate([1,2,3,1,2,3], 2))  # Output: False

# I need to check whether the same number appears at two different indices whose distance is at most k.

# I use a hash map that stores each number together with the most recent index where I’ve seen it.  

# As I walk through the array, for every number I first check if it’s already in the map.  
# If it is, I compute the distance between the current index and the stored index. 
# If that distance is ≤ k, I’ve found a nearby duplicate and can return true right away.  

# If the distance is larger than k, or if the number hasn’t appeared yet, I simply update the map with the current index. 
# Keeping only the most recent index is enough, because any future occurrence will be even farther from older positions.  

# If I finish the entire array without finding such a pair, I return false.