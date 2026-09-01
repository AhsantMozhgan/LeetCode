# https://leetcode.com/problems/snakes-and-ladders

from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        # Get Board Size
        # The board is an n x n board.
        n = len(board)

        # Convert Square Number To Board Position
        # Convert a square number such as
        # 1, 2, 3, ... into [row, column].
        def intToPos(square):

            # Convert the square number into a zero-based index.
            r = (square - 1) // n
            c = (square - 1) % n

            # Handle Zigzag Direction
            # Every other row is reversed.
            if r % 2 == 1:

                # Reverse the column.
                c = n - 1 - c

            # Convert From Bottom To Python Row Index
            # Square numbering starts from the bottom, while Python matrix indexing starts from the top.
            r = n - 1 - r

            return [r, c]

        # BFS Initialization
        # Start at square 1.
        # The second value represents the number of moves so far.
        q = deque([(1, 0)])

        # Store squares that we have already visited.
        visit = set()

        # BFS
        while q:

            # Get the next square and the number of moves used to reach it
            square, moves = q.popleft()

            # Try All Dice Rolls
            # A dice roll can move us between 1 and 6 squares.
            for i in range(1, 7):

                nextSquare = square + i

                # Convert Square To Position
                # Convert the square number into board[row][column].
                r, c = intToPos(nextSquare)

                # Handle Snake / Ladder
                # If the square contains a snake or ladder, jump to the indicated destination.
                if board[r][c] != -1:
                    nextSquare = board[r][c]

                # Check Final Square
                # If we reached n², we are finished.
                if nextSquare == n * n:
                    return moves + 1

                # Add Unvisited Square
                if nextSquare not in visit:

                    # Mark the square as visited.
                    visit.add(nextSquare)

                    # Add the square to the BFS queue.
                    # moves + 1 means this square requires one additional dice roll.
                    q.append([nextSquare, moves + 1])

        # No Solution
        # If the final square cannot be reached, return -1.
        return -1


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    board = [[-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,35,-1,-1,13,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,15,-1,-1,-1,-1],
             [-1,-1,-1,12,-1,-1]]
    result = solution.snakesAndLadders(board)
    print(result)  # Expected output: 4

# I use BFS because the goal is to find the minimum number of dice rolls needed to reach the last square. 
# Each square is a node, and from each square we can move to up to six next squares depending on the dice roll. 
# I convert the square number into row and column coordinates because the board uses a zigzag numbering pattern. 
# If the destination contains a snake or ladder, I jump to its destination. 
# I keep track of visited squares so I don't process the same square multiple times.
# Why BFS?
# Because every dice roll has the same cost, so this is a shortest-path problem in an unweighted graph. 
# BFS guarantees that we find the minimum number of moves.

# ---

# # OR
# from collections import deque
# from typing import List

# class Solution:
#     def snakesAndLadders(self, board: List[List[int]]) -> int:

#         n = len(board)
#         target = n * n

#         # BFS queue
#         queue = deque([1])

#         # Keep track of visited squares
#         visited = set([1])

#         # Number of dice rolls
#         moves = 0

#         while queue:

#             # Process one BFS level
#             for _ in range(len(queue)):

#                 current = queue.popleft()

#                 # Try all possible dice rolls
#                 for dice in range(1, 7):

#                     next_square = current + dice

#                     if next_square > target:
#                         continue

#                     # Convert square number to board[row][col]
#                     quotient, remainder = divmod(next_square - 1, n)

#                     row = n - 1 - quotient

#                     if quotient % 2 == 0:
#                         col = remainder
#                     else:
#                         col = n - 1 - remainder

#                     # Snake or ladder
#                     if board[row][col] != -1:
#                         next_square = board[row][col]

#                     # If we reached the target
#                     if next_square == target:
#                         return moves + 1

#                     # Add to BFS if not visited
#                     if next_square not in visited:
#                         visited.add(next_square)
#                         queue.append(next_square)

#             moves += 1

#         return -1
