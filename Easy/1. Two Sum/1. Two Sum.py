# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        number_to_index = dict()  # Dictionary to hold number and its index
        # num_to_index = {}
        
        for current_index, current_number in enumerate(nums):
            required_number = target - current_number  # Calculate the required_number
            if required_number in number_to_index:
                # Return indices of the two numbers
                return [number_to_index[required_number], current_index]  
            number_to_index[current_number] = current_index  # Add number to the dictionary
            
        return []  # Return an empty list if no solution is found (though problem guarantees one solution)


# -----------------------
# Example
# -----------------------

solution = Solution()

nums = [2,7,11,15]
target = 9

result = solution.twoSum(nums, target)

print(result)      # Output: [0,1]



# A brute-force solution would check every possible pair of numbers, which is O(n²). 
# To do better I use a hash map that stores each number I’ve already seen together with its index.  

# As I walk through the array I compute the complement I still need: `target - current_number`.  
# If that complement is already in the map, I return the stored index of the complement and the current index—those two numbers add up to the target.  
# If it isn’t there, I simply store the current number and its index so a later number can use it as its complement.  

# I always do the lookup *before* inserting the current number, which guarantees I never use the same element twice.  

# The whole algorithm makes a single pass, so it runs in O(n) time, and the hash map uses O(n) extra space in the worst case.
