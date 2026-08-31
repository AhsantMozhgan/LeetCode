# https://leetcode.com/problems/course-schedule-ii

# DFS
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Build Graph
        # graph[course] contains the courses that depend on this course.
        # Example:
        # [1, 0]
        # means:
        # 0 → 1
        graph = [[] for _ in range(numCourses)]

        # Add every prerequisite relationship to the graph.
        for course, prerequisite in prerequisites:

            # The prerequisite must come before the course.
            graph[prerequisite].append(course)

        # Visit States
        # 0 = Unvisited
        # 1 = Visiting
        # 2 = Visited
        state = [0] * numCourses

        # Result
        # Courses are added here after their neighbors have been completely processed.
        result = []

        # DFS
        # Returns False if a cycle is detected.
        def dfs(course):

            # Cycle Detected
            # If this course is already in the current DFS path, we found a cycle.
            if state[course] == 1:
                return False

            # Already Processed
            # This course was already completely checked.
            if state[course] == 2:
                return True

            # Mark As Visiting This course is now part of the current DFS path.
            state[course] = 1

            # Explore Neighbors
            # Visit all courses that depend on this course.
            for next_course in graph[course]:

                # If a cycle is found, the entire ordering is impossible.
                if not dfs(next_course):
                    return False

            # Mark As Visited All neighbors have been safely processed.
            state[course] = 2

            # Add To Result
            # We add the course AFTER processing its neighbors. This is called postorder.
            result.append(course)

            return True

        # Process Every Course
        # The graph may contain disconnected components.
        for course in range(numCourses):

            if not dfs(course):
                # A cycle exists, so no valid ordering exists.
                return []

        # Reverse Result
        # DFS added courses in reverse dependency order.
        # Example:
        # 0 → 1 → 2
        # DFS result:
        # [2, 1, 0]
        # Reverse:
        # [0, 1, 2]
        result.reverse()

        # Return Answer
        return result


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    numCourses = 4
    prerequisites = [[2, 0], [1, 0], [3, 1], [3, 2]]  # To take course 2 and 1, you need 0, and to take 3, you need 1 and 2
    result = solution.findOrder(numCourses, prerequisites)
    print(result)  # Expected output could be [0, 1, 2, 3] or [0, 2, 1, 3], among other valid orders


# This problem is a topological sorting problem. I build a directed graph where each prerequisite points to the course that depends on it. 
# I use DFS with three states to detect cycles. If I encounter a node that is currently being visited, there is a cycle, so I return an empty array. 
# Otherwise, after completely processing all neighbors of a course, I add that course to the result. 
# This gives me a postorder traversal, so I reverse the result at the end to get a valid course order.


# ///////////////////////////////////////////////////////////////////////////////////////
# # OR
# from collections import defaultdict, deque

# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         # Step 1: Build the graph and in-degree array
#         graph = defaultdict(list)
#         in_degree = [0] * numCourses
        
#         for course, prerequisite in prerequisites:
#             graph[prerequisite].append(course)  # Edge from prerequisite to course
#             in_degree[course] += 1  # Increment in-degree for the course
            
#         # Step 2: Initialize the queue with all courses with zero in-degree
#         queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
#         order = []

#         # Step 3: Process the courses
#         while queue:
#             current = queue.popleft()
#             order.append(current)  # Add the course to the order
            
#             # Decrease the in-degree of the neighbors
#             for neighbor in graph[current]:
#                 in_degree[neighbor] -= 1
#                 # If in-degree becomes zero, add to the queue
#                 if in_degree[neighbor] == 0:
#                     queue.append(neighbor)

#         # Step 4: Check if we could schedule all courses
#         if len(order) == numCourses:
#             return order  # Return the correct order
#         return []  # Return empty list if not all courses could be scheduled