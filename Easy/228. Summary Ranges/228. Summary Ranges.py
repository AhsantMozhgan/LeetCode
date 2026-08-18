# https://leetcode.com/problems/summary-ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # This list will store all the summarized ranges.
        result = []

        # If there are no numbers, there are no ranges.
        if not nums:
            return result

        # start_index tells us where the current consecutive range begins.
        start_index = 0

        # Start from the second element and compare it with the previous one.
        for i in range(1, len(nums)):
            # Two numbers are consecutive if the current number is exactly one greater than the previous number.
            if nums[i] == nums[i -1] + 1:
                continue

            # If the numbers are not consecutive, the previous number is the end of the current range.
            if start_index == i - 1:
                # The range contains only one number.
                result.append(str(nums[start_index]))
            else:
                # The range contains multiple numbers.
                result.append(str(nums[start_index]) + '->' + str(nums[i - 1]))

            # The current number starts a new consecutive range.
            start_index = i

        # The loop only adds a range when it finds a break.
        # Therefore, after the loop finishes, we still need to add the final range.
        if start_index == len(nums) - 1:
            result.append(str(nums[start_index]))
        else:
            # The final range contains multiple consecutive numbers.
            result.append(str(nums[start_index]) + '->' + str(nums[-1]))

        # Return all summarized ranges.
        return result


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test case
    print(solution.summaryRanges([0, 1, 2, 4, 5, 7]))  # Output: ['0->2', '4->5', '7']
    print(solution.summaryRanges([1, 2, 3, 4, 5]))  # Output: ['1->5']
    print(solution.summaryRanges([]))  # Output: []


# Because the input is already sorted and contains unique values, consecutive numbers will always sit next to each other, so I can build the ranges in a single pass.

# I keep a start index that marks the beginning of the current range. Then I walk from the second number onward, comparing each number with the one before it.

# If the current number is exactly one greater than the previous, the range is still consecutive and I simply continue.  
# As soon as that is no longer true, the previous number is the end of the range I was building.

# At that point I check the length of the range:  
# - if start and end are the same index, I just append the single number;  
# - otherwise I append it in the “start→end” format.  

# Then I move the start index forward to the current position so a new range can begin.

# After the loop I still have to handle the final range, because the loop only emits a range when it hits a gap. If the last few numbers were consecutive, t
# here was no later gap to trigger that emission, so I append the last range once the loop finishes.
