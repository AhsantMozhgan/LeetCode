# https://leetcode.com/problems/word-ladder

from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
       
        # Check If Target Exists
        # If endWord is not in the word list, we can never reach it.
        if endWord not in wordList:
            return 0

        # Convert Word List To A Set
        # A set gives us fast lookup when checking whether a word exists in the word list.
        word_set = set(wordList)

        # BFS Initialization
        # Store the current word and the number of words in the transformation sequence.
        queue = deque([(beginWord, 1)])

        # Store words that we have already visited.
        visited = {beginWord}

        # BFS
        while queue:

            # Get the current word and current sequence length.
            current_word, steps = queue.popleft()

            # Check Target
            # Check if we have reached the endWord
            if current_word == endWord:
                return steps

            # Try Every Character Position
            for i in range(len(current_word)):

                # Try every possible lowercase English letter.
                for char in "abcdefghijklmnopqrstuvwxyz":

                    # Create a new word by changing one character.
                    next_word = (current_word[:i] + char + current_word[i + 1:])

                    # Check Valid Word 
                    # The new word must:
                    # 1. Exist in word_set
                    # 2. Not have been visited
                    if (next_word in word_set and next_word not in visited):

                        # Mark the word as visited.
                        visited.add(next_word)

                        # Add the word to BFS.
                        queue.append((next_word, steps + 1))

        # No Transformation
        return 0

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    result = solution.ladderLength(beginWord, endWord, wordList)
    print(result)  # Expected output: 5

# I treat each word as a node in an unweighted graph. Two words are connected if they differ by exactly one character. 
# I use BFS because I need the shortest transformation sequence. Instead of comparing every pair of words, 
# for each current word I generate all possible words by changing each character to each of the 26 lowercase letters. 
# If the generated word exists in the word set and hasn't been visited, I add it to the BFS queue. 
# The first time I reach the end word, I return the sequence length.
