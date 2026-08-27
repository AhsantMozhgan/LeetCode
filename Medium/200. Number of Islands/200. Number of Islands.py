# https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:  # Edge case for empty grid
            return 0
        
        num_rows = len(grid)
        num_cols = len(grid[0])
        island_count = 0
        
        # Helper function to perform DFS
        def dfs(r, c):
            # Check for out-of-bounds or water '0'
            if r < 0 or r >= num_rows or c < 0 or c >= num_cols or grid[r][c] == '0':
                return
            
            # Mark the cell as visited
            grid[r][c] = '0'
            
            # Explore its neighboring cells (up, down, left, right)
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        # Iterate through each cell in the grid
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == '1':  # Found an island
                    island_count += 1  # Increment the count
                    dfs(row, col)      # Sink the entire island

        return island_count

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(solution.numIslands(grid1))  # Output: 3

    grid2 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(solution.numIslands(grid2))  # Output: 1


# I scan the entire grid. Whenever I find a land cell that hasn't been visited, I know I've found a new island, so I increment the island count. 
# Then I run DFS from that cell to explore all connected land cells in the four possible directions. 
# I mark each visited land cell as water so I don't process the same island again.


# ---

# OR
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
        # if not grid:
        #     return 0

        # total_rows = len(grid)
        # total_cols = len(grid[0])

        # island_count = 0

        # for current_row in range(total_rows):
        #     for current_col in range(total_cols):

        #         # Skip water or already visited land
        #         if grid[current_row][current_col] == "0":
        #             continue

        #         # Found a new island
        #         island_count += 1

        #         # Start BFS
        #         cells_to_visit = deque()
        #         cells_to_visit.append((current_row, current_col))

        #         # Mark as visited immediately
        #         grid[current_row][current_col] = "0"

        #         while cells_to_visit:

        #             row, col = cells_to_visit.popleft()

        #             # Explore the four directions
        #             directions = [
        #                 (-1, 0),   # Up
        #                 (1, 0),    # Down
        #                 (0, -1),   # Left
        #                 (0, 1),    # Right
        #             ]

        #             for row_offset, col_offset in directions:

        #                 next_row = row + row_offset
        #                 next_col = col + col_offset

        #                 # Skip cells outside the grid
        #                 if (
        #                     next_row < 0
        #                     or next_row >= total_rows
        #                     or next_col < 0
        #                     or next_col >= total_cols
        #                 ):
        #                     continue

        #                 # Skip water or visited cells
        #                 if grid[next_row][next_col] == "0":
        #                     continue

        #                 # Mark as visited and add to queue
        #                 grid[next_row][next_col] = "0"
        #                 cells_to_visit.append((next_row, next_col))

        # return island_count

