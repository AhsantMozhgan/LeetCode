# https://leetcode.com/problems/find-median-from-data-stream

# class MedianFinder:

#     def __init__(self):
        

#     def addNum(self, num: int) -> None:
        

#     def findMedian(self) -> float:
        


# # Your MedianFinder object will be instantiated and called as such:
# # obj = MedianFinder()
# # obj.addNum(num)
# # param_2 = obj.findMedian()


from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):

        # Max Heap for the smaller half.
        # Python only provides a Min Heap, so we store negative values.
        self.small = []

        # Min Heap for the larger half.
        self.large = []


    def addNum(self, num: int) -> None:

        # Add To Small Heap
        # Store negative value so Python's Min Heap behaves like a Max Heap.
        heappush(self.small, -num)

        # Move Largest Small Value To Large Heap
        # The largest value in small should be <= the smallest value in large.
        if self.small and self.large:

            if -self.small[0] > self.large[0]:

                largest_small = -heappop(self.small)

                heappush(self.large, largest_small)

        # Balance The Heaps
        # small can have at most one more element than large.
        if len(self.small) > len(self.large) + 1:

            value = -heappop(self.small)

            heappush(self.large, value)

        elif len(self.large) > len(self.small):

            value = heappop(self.large)

            heappush(self.small, -value)


    def findMedian(self) -> float:

        # Odd Number Of Elements
        if len(self.small) > len(self.large):

            return float(-self.small[0])

        # Even Number Of Elements
        return (-self.small[0] + self.large[0]) / 2.0


# Example usage
if __name__ == "__main__":
    medianFinder = MedianFinder()
    
    medianFinder.addNum(1)
    print(medianFinder.findMedian())  # Output: 1.0
    medianFinder.addNum(2)
    print(medianFinder.findMedian())  # Output: 1.5
    medianFinder.addNum(3)
    print(medianFinder.findMedian())  # Output: 2.0
    

# I use two heaps to maintain the lower and upper halves of the numbers. The lower half is stored in a max heap, and the upper half is stored in a min heap. 
# I maintain two conditions: the sizes of the heaps differ by at most one, and every value in the max heap is less than or equal to every value in the min heap. 
# When a number is added, I insert it into the max heap, fix the ordering if necessary, and then rebalance the two heaps. 
# If the total number of elements is odd, the median is the top of the max heap. 
# If it is even, the median is the average of the tops of the two heaps. `addNum` takes O(log n) and `findMedian` takes O(1).



# # ---
# # OR
# import heapq

# class MedianFinder:
#     def __init__(self):
#         # Max-heap for the lower half
#         self.lower_half = []  # max-heap (inverted)
#         # Min-heap for the upper half
#         self.upper_half = []  # min-heap

#     def addNum(self, num: int) -> None:
#         # Add to max-heap (lower half)
#         heapq.heappush(self.lower_half, -num)
        
#         # Balance: Ensure the largest of lower half is less than the smallest of upper half
#         if (self.lower_half and self.upper_half and 
#             (-self.lower_half[0] > self.upper_half[0])):
#             value = -heapq.heappop(self.lower_half)
#             heapq.heappush(self.upper_half, value)
        
#         # Balance the sizes of the heaps
#         if len(self.lower_half) > len(self.upper_half) + 1:
#             value = -heapq.heappop(self.lower_half)
#             heapq.heappush(self.upper_half, value)
#         elif len(self.upper_half) > len(self.lower_half):
#             value = heapq.heappop(self.upper_half)
#             heapq.heappush(self.lower_half, -value)

#     def findMedian(self) -> float:
#         if len(self.lower_half) > len(self.upper_half):
#             return float(-self.lower_half[0])
#         return (-self.lower_half[0] + self.upper_half[0]) / 2.0
