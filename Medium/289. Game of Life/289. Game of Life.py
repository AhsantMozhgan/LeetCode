# https://leetcode.com/problems/game-of-life

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        columns = len(board[0])

        # ------------------------------------------------
        # Direction of the 8 possible neighboring cells
        # ------------------------------------------------
        #
        # Every cell can have up to 8 neighbors:
        #
        # ↖  ↑  ↗
        # ←  X  →
        # ↙  ↓  ↘
        #
        directions = [
            (-1, -1),  # Upper-left
            (-1, 0),   # Up
            (-1, 1),   # Upper-right
            (0, -1),   # Left
            (0, 1),    # Right
            (1, -1),   # Lower-left
            (1, 0),    # Down
            (1, 1)     # Lower-right
        ]


        # ------------------------------------------------
        # Process every cell
        # ------------------------------------------------

        for row in range(rows):
            for column in range(columns):

                live_neighbors = 0

                # Check all 8 neighboring cells.
                for row_change, column_change in directions:

                    neighbor_row = row + row_change
                    neighbor_column = column + column_change

                    # Make sure the neighbor is inside
                    # the boundaries of the board.
                    if (
                        0 <= neighbor_row < rows
                        and 0 <= neighbor_column < columns
                    ):

                        # We only care about whether the
                        # neighbor was ALIVE in the original
                        # generation.
                        #
                        # board value:
                        #
                        # 0 = originally dead
                        # 1 = originally alive
                        # 2 = originally alive, becomes dead
                        # 3 = originally dead, becomes alive
                        #
                        if board[neighbor_row][neighbor_column] in (1, 2):
                            live_neighbors += 1


                # ------------------------------------------------
                # Apply Game of Life Rules
                # ------------------------------------------------
                #
                # Rule 1:
                # A live cell with fewer than 2 live neighbors
                # dies because of underpopulation.
                #
                # Rule 2:
                # A live cell with 2 or 3 live neighbors
                # survives.
                #
                # Rule 3:
                # A live cell with more than 3 live neighbors
                # dies because of overpopulation.
                #
                # Rule 4:
                # A dead cell with exactly 3 live neighbors
                # becomes alive.
                #

                if board[row][column] == 1:

                    # Live cell dies if it has
                    # fewer than 2 or more than 3
                    # live neighbors.
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[row][column] = 2

                else:

                    # Dead cell becomes alive if it has
                    # exactly 3 live neighbors.
                    if live_neighbors == 3:
                        board[row][column] = 3


        # ------------------------------------------------
        # Convert encoded states into final states
        # ------------------------------------------------
        #
        # 0 -> 0
        # 1 -> 1
        # 2 -> 0
        # 3 -> 1
        #
        # We only need the final state now.
        #
        for row in range(rows):
            for column in range(columns):

                if board[row][column] == 2:
                    board[row][column] = 0

                elif board[row][column] == 3:
                    board[row][column] = 1

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Example board
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]

    solution.gameOfLife(board)
    print(board)  # Output: [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]



# The challenge is that Game of Life updates must be applied simultaneously. 
# If I changed cells directly from 0 to 1 or 1 to 0, later cells could count an already-updated neighbor instead of its original state.  

# To solve this in place I introduce two temporary states:  
# - 2 means the cell was originally alive but will die,  
# - 3 means the cell was originally dead but will become alive.  

# For every cell I examine its eight possible neighbors. 
# When I count live neighbors I treat both 1 and 2 as live, because both represent cells that were alive in the original generation.  

# Then I apply the classic rules:  
# - A live cell with fewer than two or more than three live neighbors dies → I mark it 2.  
# - A dead cell with exactly three live neighbors becomes alive → I mark it 3.  

# After processing the entire board I make a final pass that converts the temporary states: 2 becomes 0 and 3 becomes 1.  

# The algorithm runs in O(m × n) time (each cell examines at most eight neighbors) and uses only O(1) extra space because the transition states live directly in the board.
