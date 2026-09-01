# https://leetcode.com/problems/implement-trie-prefix-tree

# class Trie:

#     def __init__(self):
        

#     def insert(self, word: str) -> None:
        

#     def search(self, word: str) -> bool:
        

#     def startsWith(self, prefix: str) -> bool:
        


# # Your Trie object will be instantiated and called as such:
# # obj = Trie()
# # obj.insert(word)
# # param_2 = obj.search(word)
# # param_3 = obj.startsWith(prefix)


class TrieNode:

    def __init__(self):

        # Store the children of this node.
        # The key is a character and the value is the next TrieNode.
        self.children = {}

        # True means a complete word ends at this node.
        self.is_end = False


class Trie:

    def __init__(self):

        # Create the root node.
        # Root does not represent any character.
        self.root = TrieNode()

    # Insert
    def insert(self, word: str) -> None:

        # Start from the root.
        current = self.root

        # Process each character in the word.
        for char in word:

            # If this character does not already exist as a child, create a new node.
            if char not in current.children:
                current.children[char] = TrieNode()

            # Move to the next node.
            current = current.children[char]

        # Mark the final node as the end of a complete word.
        current.is_end = True

    # Search
    def search(self, word: str) -> bool:

        # Start from the root.
        current = self.root

        # Traverse through every character in the word.
        for char in word:

            # If the character does not exist, the word is not stored.
            if char not in current.children:
                return False

            # Move to the next node.
            current = current.children[char]

        # The entire word must end here.
        return current.is_end

    # Starts With
    def startsWith(self, prefix: str) -> bool:

        # Start from the root.
        current = self.root

        # Traverse through every character in the prefix.
        for char in prefix:

            # If any character is missing, no word starts with this prefix.
            if char not in current.children:
                return False

            # Move to the next node.
            current = current.children[char]

        # We successfully traversed the entire prefix.
        return True

# Example Usage
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))   # True
    print(trie.search("app"))     # False
    print(trie.startsWith("app"))  # True
    trie.insert("app")
    print(trie.search("app"))     # True

# I implement a Trie using TrieNode objects. Each node stores a dictionary of children and a boolean indicating whether a complete word ends at that node. 
# For insertion, I traverse each character and create a node if it doesn't already exist. 
# For search, I traverse the characters and return whether the final node marks the end of a word. 
# For startsWith, I only need to verify that the entire prefix path exists, so I don't need to check `is_end`.
