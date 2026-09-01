# https://leetcode.com/problems/design-add-and-search-words-data-structure

# class WordDictionary:

#     def __init__(self):
        

#     def addWord(self, word: str) -> None:
        

#     def search(self, word: str) -> bool:
        


# # Your WordDictionary object will be instantiated and called as such:
# # obj = WordDictionary()
# # obj.addWord(word)
# # param_2 = obj.search(word)


class TrieNode:

    def __init__(self):

        # Store the child nodes.
        # Each key is a character.
        self.children = {}

        # True means a complete word ends at this node.
        self.is_end = False


class WordDictionary:

    def __init__(self):

        # Create the root node.
        self.root = TrieNode()

    # Add Word
    def addWord(self, word: str) -> None:

        # Start from the root.
        current = self.root

        # Process every character.
        for char in word:

            # Create a new node if the character does not exist.
            if char not in current.children:
                current.children[char] = TrieNode()

            # Move to the next node.
            current = current.children[char]

        # Mark the final node as the end of a complete word.
        current.is_end = True

    # Search
    def search(self, word: str) -> bool:

        # Use DFS to search through the Trie.
        def dfs(index: int, node: TrieNode) -> bool:

            # Base Case
            # We have processed every character in the word.
            if index == len(word):

                # The word must end at this Trie node.
                return node.is_end

            # Get the current character.
            char = word[index]

            # Normal Character
            if char != ".":

                # If this character does not exist, the word cannot be found.
                if char not in node.children:
                    return False

                # Continue searching with the matching child.
                return dfs(index + 1, node.children[char])

            # Wildcard Character
            # "." can represent any character.
            for child in node.children.values():

                # Try this possible character.
                if dfs(index + 1, child):
                    return True

            # None of the possible characters worked.
            return False


        # Start DFS from the root.
        return dfs(0, self.root)


# Example Usage
if __name__ == "__main__":
    wordDict = WordDictionary()
    wordDict.addWord("bad")
    wordDict.addWord("dad")
    wordDict.addWord("mad")
    
    print(wordDict.search("pad"))  # False
    print(wordDict.search("bad"))  # True
    print(wordDict.search(".ad"))  # True
    print(wordDict.search("b.."))  # True

# I use a Trie to store all the words. Each Trie node contains a dictionary of children and an `is_end` flag. 
# Adding a word is the same as a normal Trie insertion. For searching, normal characters follow one specific child. 
# However, when I encounter `.`, it can represent any character, so I recursively search all child nodes using DFS. 
# If any branch reaches the end of the word at a node marked `is_end`, the search returns true.


# ---
# OR
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_of_word = False

# class WordDictionary:
#     def __init__(self):
#         self.root = TrieNode()

#     def addWord(self, word: str) -> None:
#         current = self.root
#         for char in word:
#             if char not in current.children:
#                 current.children[char] = TrieNode()
#             current = current.children[char]
#         current.is_end_of_word = True

#     def search(self, word: str) -> bool:
#         return self._search_in_node(word, self.root)

#     def _search_in_node(self, word: str, node: TrieNode) -> bool:
#         for i, char in enumerate(word):
#             if char == '.':
#                 # Check all possibilities for the current node's children
#                 for child in node.children.values():
#                     if self._search_in_node(word[i + 1:], child):
#                         return True
#                 return False
#             else:
#                 if char not in node.children:
#                     return False
#                 node = node.children[char]
#         return node.is_end_of_word
