# https://leetcode.com/problems/find-k-pairs-with-smallest-sums

from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        # Handle Empty Input
        if not nums1 or not nums2 or k <= 0:
            return []

        # Store the result pairs.
        result = []

        # Min heap.
        # Each element is:
        # (sum, index1, index2)
        min_heap = []

        # Initialize The Heap
        # Pair each of the first min(k, len(nums1)) elements with nums2[0].
        for i in range(min(k, len(nums1))):

            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))


        # Find K Smallest Pairs
        while min_heap and len(result) < k:

            # Get the pair with the smallest sum.
            current_sum, i, j = heapq.heappop(min_heap)

            # Add the pair to the result.
            result.append([nums1[i], nums2[j]])

            # Move To The Next Pair
            # For the same nums1[i], try the next element in nums2.
            if j + 1 < len(nums2):

                heapq.heappush(min_heap,(nums1[i] + nums2[j + 1], i, j + 1))

        return result



# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.kSmallestPairs([1, 7], [3, 5, 8], 3))  # Output: [(1, 3), (1, 5), (1, 8)]
    print(solution.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))  # Output: [(1, 1), (1, 1)]
    print(solution.kSmallestPairs([], [1, 2], 2))  # Output: []

# Both arrays are sorted, so for each element in nums1, the pairs formed with nums2 are also sorted by their sums. 
# I use a min heap to perform a k-way merge of these sorted sequences. Initially, I add the pair of each of the first min(k, len(nums1)) elements of nums1 with nums2[0]. 
# Each heap entry stores the sum and the two indices. I repeatedly remove the pair with the smallest sum, add it to the result, and then add the next pair from the same row by incrementing the nums2 index. 
# I stop after k pairs. The time complexity is O(k log k) and the space complexity is O(k).



# # ---
# # OR
# import heapq
# from typing import List, Tuple

# class Solution:
#     def kSmallestPairs(self, A: List[int], B: List[int], k: int) -> List[Tuple[int, int]]:
#         result = []
#         if not A or not B or k <= 0:
#             return result
        
#         # Min-Heap
#         min_heap = []
        
#         # Initialize the heap with the first element of A paired with all elements in B
#         for j in range(min(k, len(B))):  # Only need to consider the first k elements of B
#             heapq.heappush(min_heap, (A[0] + B[j], 0, j))  # (sum, index in A, index in B)

#         # Extract k pairs from the heap
#         while k > 0 and min_heap:
#             sum_ab, i, j = heapq.heappop(min_heap)  # Get the smallest pair
#             result.append((A[i], B[j]))

#             # If there's a next element in A, push the pair of next element from A with B[j]
#             if i + 1 < len(A):
#                 heapq.heappush(min_heap, (A[i + 1] + B[j], i + 1, j))

#             k -= 1

#         return result

# # Example usage
# if __name__ == "__main__":
#     solution = Solution()
    
#     print(solution.kSmallestPairs([1, 7], [3, 5, 8], 3))  # Output: [(1, 3), (1, 5), (1, 8)]
#     print(solution.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))  # Output: [(1, 1), (1, 1)]
#     print(solution.kSmallestPairs([], [1, 2], 2))  # Output: []

