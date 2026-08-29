# https://leetcode.com/problems/surrounded-regions

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board:  # Handle empty board
            return
        
        num_rows = len(board)  # Get the number of rows
        num_cols = len(board[0])  # Get the number of columns

        # Define the DFS function
        def dfs(r, c):
            # Check for out-of-bounds and if the cell is 'O'
            if r < 0 or r >= num_rows or c < 0 or c >= num_cols or board[r][c] != 'O':
                return
            
            # Mark the cell as visited by changing 'O' to a temporary marker 'T'
            board[r][c] = 'T'
            
            # Explore neighbors
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        # Traverse the borders
        for r in range(num_rows):
            for c in range(num_cols):
                # Check first and last rows
                if (r == 0 or r == num_rows - 1) and board[r][c] == 'O':
                    dfs(r, c)
                # Check first and last columns
                if (c == 0 or c == num_cols - 1) and board[r][c] == 'O':
                    dfs(r, c)

        # Final pass to capture surrounded regions
        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # Change surrounded 'O' to 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'  # Change temporary 'T' back to 'O'



# Example Usage
if __name__ == "__main__":
    solution = Solution()
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    solution.solve(board)
    for row in board:
        print(row)  # Expected Output: [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]

# Instead of finding the surrounded regions, I find the regions that cannot be surrounded.
# The key observation is that any O connected to the border cannot be surrounded. So instead of searching for surrounded regions directly, I start DFS from every border O and mark all connected O's as safe. 
# I temporarily change those cells to S. After that, any remaining O must be surrounded, so I change it to X. Finally, I change all S cells back to O.
 