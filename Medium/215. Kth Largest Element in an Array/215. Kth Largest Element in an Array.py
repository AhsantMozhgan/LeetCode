# https://leetcode.com/problems/kth-largest-element-in-an-array

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # Keep K Largest Elements
        # Create a min heap.
        min_heap = []

        # Process Every Number
        for number in nums:

            # Add the current number to the heap.
            heapq.heappush(min_heap, number)

            # Keep Only K Elements
            # If we have more than k elements, remove the smallest.
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Kth Largest Element
        # The smallest element inside the K largest elements is the Kth largest overall.
        return min_heap[0]


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # Output: 5
    print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # Output: 4

# I use a min heap of size k. I iterate through every number and add it to the heap. 
# If the heap becomes larger than k, I remove the smallest element. This guarantees that the heap always contains the k largest elements seen so far. 
# At the end, the smallest element in the heap is the kth largest element overall. The time complexity is O(n log k) and the space complexity is O(k).


# # ------
# # OR
# # Min-Heap Approach
# import heapq

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         # Create a min-heap with the first k elements
#         min_heap = nums[:k]
#         heapq.heapify(min_heap)

#         # Iterate through the remaining elements
#         for num in nums[k:]:
#             if num > min_heap[0]:  # Compare with the smallest element in the heap
#                 heapq.heappop(min_heap)  # Remove the smallest
#                 heapq.heappush(min_heap, num)  # Add the new element

#         # The root of the min-heap is the k-th largest element
#         return min_heap[0]



# # ---
# # OR
# # Quickselect Approach
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         def quickselect(left, right, k_smallest):
#             # Select a random pivot
#             pivot = nums[right]
#             # Partitioning
#             partition_index = left
#             for i in range(left, right):
#                 if nums[i] >= pivot:  # We want k-th largest, so we use >=
#                     nums[i], nums[partition_index] = nums[partition_index], nums[i]
#                     partition_index += 1
#             # Move pivot to its final place
#             nums[partition_index], nums[right] = nums[right], nums[partition_index]

#             # Recursively apply the algorithm
#             if partition_index == k_smallest:
#                 return nums[partition_index]
#             elif partition_index < k_smallest:
#                 return quickselect(partition_index + 1, right, k_smallest)
#             else:
#                 return quickselect(left, partition_index - 1, k_smallest)

#         n = len(nums)
#         # Convert k to the kth largest index (0-based)
#         return quickselect(0, n - 1, n - k)
