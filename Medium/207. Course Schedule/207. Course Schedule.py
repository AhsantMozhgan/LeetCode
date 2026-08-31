# https://leetcode.com/problems/course-schedule

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build the adjacency list for the graph
        graph = defaultdict(list)
        
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        # Step 2: Create a visitation state array
        visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited
        
        def dfs(course):
            if visited[course] == 1:  # Cycle detected
                return False
            if visited[course] == 2:  # Already fully explored
                return True
            
            # Mark the course as visiting
            visited[course] = 1  
            
            # Visit all the neighbors (courses dependent on this course)
            for neighbor in graph[course]:
                if not dfs(neighbor):  # If a cycle is detected
                    return False
            
            # Mark the course as fully visited
            visited[course] = 2
            return True

        # Step 3: Check every course
        for i in range(numCourses):
            if visited[i] == 0:  # Unvisited
                if not dfs(i):  # If any DFS returns False, then we cannot finish all courses
                    return False

        return True

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    numCourses = 2
    prerequisites = [[1, 0]]  # To take course 1, you must complete course 0
    result = solution.canFinish(numCourses, prerequisites)
    print(result)  # Expected output: True


# I model the courses as nodes in a directed graph. For each prerequisite `[course, prerequisite]`, I add a directed edge from the prerequisite to the course. 
# The key observation is that we can finish all courses if and only if the graph has no cycle. I use DFS with three states: unvisited, visiting, and visited. 
# If I reach a node that is currently visiting, I found a cycle and return false. If a node is already fully visited, I can skip it because it has already been checked. 
# After exploring all neighbors, I mark the current course as fully visited. If no cycle is found, I return true.


# ---
# OR
# DFS + Cycle Detection
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

#         # course -> prerequisite courses
#         prerequisite_graph = defaultdict(list)

#         for course, prerequisite in prerequisites:
#             prerequisite_graph[course].append(prerequisite)

#         completed_courses = set()
#         current_path = set()

#         def has_cycle(course):

#             # Already completely checked
#             if course in completed_courses:
#                 return False

#             # Found a cycle
#             if course in current_path:
#                 return True

#             current_path.add(course)

#             for prerequisite in prerequisite_graph[course]:
#                 if has_cycle(prerequisite):
#                     return True

#             current_path.remove(course)
#             completed_courses.add(course)

#             return False

#         for course in range(numCourses):
#             if has_cycle(course):
#                 return False

#         return True

# ---

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

#         # BFS + Topological Sort
#         # prerequisite_graph[course] = courses unlocked after finishing 'course'
#         prerequisite_graph = [[] for _ in range(numCourses)]

#         # Number of prerequisites each course still needs
#         remaining_prerequisites = [0] * numCourses

#         # Build the graph and count prerequisites
#         for course, prerequisite in prerequisites:
#             prerequisite_graph[prerequisite].append(course)
#             remaining_prerequisites[course] += 1

#         # Courses that are ready to be taken
#         available_courses = deque()

#         for course in range(numCourses):
#             if remaining_prerequisites[course] == 0:
#                 available_courses.append(course)

#         completed_courses = 0

#         while available_courses:

#             current_course = available_courses.popleft()
#             completed_courses += 1

#             # Completing the current course satisfies one prerequisite
#             # for every course that depends on it.
#             for next_course in prerequisite_graph[current_course]:

#                 remaining_prerequisites[next_course] -= 1

#                 if remaining_prerequisites[next_course] == 0:
#                     available_courses.append(next_course)

#         return completed_courses == numCourses
