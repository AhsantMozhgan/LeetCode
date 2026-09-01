# https://leetcode.com/problems/word-search-ii

from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Store all words that we find.
        result = []

        # Get the number of rows and columns in the board.
        m, n = len(board), len(board[0])

        # Build Trie
        # Each dictionary represents one Trie node.
        trie = {}

        for word in words:

            # Start from the root of the Trie.
            node = trie

            # Add every character of the word to the Trie.
            for ch in word:

                # If this character does not already exist, create a new node.
                if ch not in node:
                    node[ch] = {}

                # Move to the next Trie node.
                node = node[ch]

            # Store the complete word at the final Trie node.
            node["word"] = word

        # DFS / Backtracking
        def dfs(row, col, node):

            # Get the character at the current board position.
            ch = board[row][col]

            # If this character is not in the current Trie node, this path cannot form a word.
            if ch not in node:
                return

            # Move to the Trie node corresponding to this character.
            next_node = node[ch]

            # Check Complete Word
            # If "word" exists in this Trie node, we have found a complete word.
            if "word" in next_node:

                # Add the word to the result.
                result.append(next_node["word"])

                # Delete the word so that we don't add it again.
                del next_node["word"]

            # Mark Cell As Visited
            # Temporarily replace the character so we cannot use this cell again during this DFS path.
            board[row][col] = ""

            # Explore Neighbors
            # Up
            if row > 0:
                dfs(row - 1, col, next_node)

            # Down
            if row + 1 < m:
                dfs(row + 1, col, next_node)

            # Left
            if col > 0:
                dfs(row, col - 1, next_node)

            # Right
            if col + 1 < n:
                dfs(row, col + 1, next_node)

            # Backtrack
            # Restore the original character so this cell can be used again in another path.
            board[row][col] = ch

        # Start DFS From Every Cell
        # Start searching from every position on the board.
        for row in range(m):

            for col in range(n):

                dfs(row, col, trie)

        # Return all words found.
        return result

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    result = solution.findWords(board, words)
    print(result)  # Expected output: ["eat", "oath"]

# I first build a Trie containing all the words. Then I run DFS from every cell on the board. During DFS, I simultaneously traverse the board and the Trie. 
# If the current character doesn't exist in the current Trie node, I stop exploring that path because no word can be formed from that prefix. 
# If the Trie node contains a complete word, I add it to the result and delete the word from the Trie to avoid duplicates.
#  I temporarily mark each board cell as visited, explore the four directions, and then restore the cell during backtracking.


# ---
# OR

# from typing import List

# class TrieNode:

#     def __init__(self):

#         # Store child nodes.
#         #
#         # Each key is a character.
#         #
#         self.children = {}

#         # Store the complete word when
#         # a word ends at this node.
#         #
#         self.word = None


# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

#         # -----------------------
#         # Build Trie
#         # -----------------------
#         #
#         # Store all words in a Trie
#         # so we can search many words
#         # efficiently.
#         #
#         root = TrieNode()


#         for word in words:

#             current = root

#             for char in word:

#                 if char not in current.children:
#                     current.children[char] = TrieNode()

#                 current = current.children[char]


#             # Store the complete word
#             # at the final Trie node.
#             #
#             current.word = word


#         # -----------------------
#         # Board Information
#         # -----------------------
#         #
#         rows = len(board)
#         cols = len(board[0])


#         # Store all words that we find.
#         #
#         result = []


#         # -----------------------
#         # DFS / Backtracking
#         # -----------------------
#         #
#         def dfs(row: int, col: int, node: TrieNode):

#             # Get the current character.
#             #
#             char = board[row][col]


#             # -----------------------
#             # Check Trie Path
#             # -----------------------
#             #
#             # If the current character
#             # is not a child of this Trie node,
#             # this path cannot form a word.
#             #
#             if char not in node.children:
#                 return


#             # Move to the Trie node
#             # corresponding to this character.
#             #
#             next_node = node.children[char]


#             # -----------------------
#             # Found A Complete Word
#             # -----------------------
#             #
#             if next_node.word is not None:

#                 result.append(next_node.word)

#                 # Remove the word so that
#                 # we do not add it again.
#                 #
#                 next_node.word = None


#             # -----------------------
#             # Mark Cell As Visited
#             # -----------------------
#             #
#             # Temporarily replace the character
#             # so we cannot use this cell again
#             # during the current path.
#             #
#             board[row][col] = "#"


#             # -----------------------
#             # Explore Neighbors
#             # -----------------------
#             #
#             directions = [
#                 (1, 0),    # down
#                 (-1, 0),   # up
#                 (0, 1),    # right
#                 (0, -1)    # left
#             ]


#             for row_change, col_change in directions:

#                 next_row = row + row_change
#                 next_col = col + col_change


#                 # Check if the neighbor is
#                 # inside the board and has not
#                 # already been visited.
#                 #
#                 if (
#                     0 <= next_row < rows
#                     and
#                     0 <= next_col < cols
#                     and
#                     board[next_row][next_col] != "#"
#                 ):

#                     dfs(
#                         next_row,
#                         next_col,
#                         next_node
#                     )


#             # -----------------------
#             # Backtrack
#             # -----------------------
#             #
#             # Restore the original character
#             # so this cell can be used again
#             # by another search path.
#             #
#             board[row][col] = char


#         # -----------------------
#         # Start DFS From Every Cell
#         # -----------------------
#         #
#         for row in range(rows):

#             for col in range(cols):

#                 dfs(row, col, root)


#         return result


# I first build a Trie from all the words. Then I run DFS from every cell on the board. During DFS, I simultaneously traverse the board and the Trie. If the current board character is not a child of the current Trie node, I stop exploring that path because no word can be formed from it. When I reach a Trie node containing a complete word, I add that word to the result. I temporarily mark each board cell as visited during the current path and restore it when backtracking. I also remove a found word from the Trie node to avoid returning duplicates.

# ---
# OR
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_of_word = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word: str) -> None:
#         current = self.root
#         for char in word:
#             if char not in current.children:
#                 current.children[char] = TrieNode()
#             current = current.children[char]
#         current.is_end_of_word = True

# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         results = set()  # Use a set to avoid duplicates
#         trie = Trie()

#         # Insert all words into the trie
#         for word in words:
#             trie.insert(word)

#         # Directions for moving in the board
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
#         # DFS function to explore the board
#         def dfs(x: int, y: int, node: TrieNode, path: str):
#             if node.is_end_of_word:
#                 results.add(path)  # A word is formed, add to results
#                 node.is_end_of_word = False  # Avoid duplicate adding

#             if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
#                 return  # Out of bounds
#             if board[x][y] == "#":  # Already visited
#                 return  # Skip the visited cell
            
#             char = board[x][y]
#             if char not in node.children:
#                 return  # No match for this path
            
#             board[x][y] = "#"  # Mark this cell as visited

#             for dx, dy in directions:
#                 # Move in all four possible directions
#                 dfs(x + dx, y + dy, node.children[char], path + char)

#             board[x][y] = char  # Unmark this cell

#         # Start DFS from each cell in the board
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 dfs(i, j, trie.root, "")

#         return list(results)
