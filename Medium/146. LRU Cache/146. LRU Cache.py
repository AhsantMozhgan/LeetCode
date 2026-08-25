# https://leetcode.com/problems/lru-cache


# class LRUCache:

#     def __init__(self, capacity: int):
        

#     def get(self, key: int) -> int:
        

#     def put(self, key: int, value: int) -> None:
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    # -----------------------
    # Constructor
    # -----------------------
    #
    # capacity tells us
    # how many items the cache
    # can store.
    #
    def __init__(self, capacity: int):

        self.capacity = capacity

        # Dictionary:
        #
        # key → Node
        #
        # This gives us O(1) lookup.
        #
        self.cache = {}

        # Dummy nodes.
        #
        # left  = Least Recently Used side
        # right = Most Recently Used side
        #
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # Initially the two dummy nodes
        # point to each other.
        #
        self.left.next = self.right
        self.right.prev = self.left


    # -----------------------
    # Remove a Node
    # -----------------------
    #
    # Remove a node from
    # the doubly linked list.
    #
    def remove(self, node):

        previous_node = node.prev
        next_node = node.next

        previous_node.next = next_node
        next_node.prev = previous_node


    # -----------------------
    # Insert at the Right
    # -----------------------
    #
    # Insert a node immediately
    # before the right dummy node.
    #
    # This means the node becomes
    # the Most Recently Used node.
    #
    def insert(self, node):

        previous_node = self.right.prev

        previous_node.next = node
        node.prev = previous_node

        node.next = self.right
        self.right.prev = node


    # -----------------------
    # Get
    # -----------------------
    #
    # Return the value for key.
    #
    def get(self, key: int) -> int:

        # Key does not exist.
        #
        if key not in self.cache:
            return -1

        # Get the existing node.
        #
        node = self.cache[key]

        # This node was just used,
        # so it becomes Most Recently Used.
        #
        self.remove(node)
        self.insert(node)

        return node.value


    # -----------------------
    # Put
    # -----------------------
    #
    # Add or update a key-value pair.
    #
    def put(self, key: int, value: int) -> None:

        # If the key already exists,
        # remove its old node first.
        #
        if key in self.cache:
            self.remove(self.cache[key])

        # Create a new node.
        #
        node = Node(key, value)

        # Store the node in the dictionary.
        #
        self.cache[key] = node

        # New nodes are Most Recently Used.
        #
        self.insert(node)


        # -----------------------
        # Check Capacity
        # -----------------------
        #
        # If we have exceeded capacity,
        # remove the Least Recently Used node.
        #
        if len(self.cache) > self.capacity:

            # The first real node after
            # the left dummy is the LRU node.
            #
            least_recently_used = self.left.next

            # Remove it from the linked list.
            #
            self.remove(least_recently_used)

            # Remove it from the dictionary.
            #
            del self.cache[least_recently_used.key]


# Example usage
if __name__ == "__main__":
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)                    # cache is {1=1}
    lru_cache.put(2, 2)                    # cache is {1=1, 2=2}
    print(lru_cache.get(1))                 # returns 1
    lru_cache.put(3, 3)                    # evicts key 2, cache is {1=1, 3=3}
    print(lru_cache.get(2))                 # returns -1 (not found)
    lru_cache.put(4, 4)                    # evicts key 1, cache is {4=4, 3=3}
    print(lru_cache.get(1))                 # returns -1 (not found)
    print(lru_cache.get(3))                 # returns 3
    print(lru_cache.get(4))                 # returns 4


#  I use a HashMap and a doubly linked list. The HashMap maps each key to its corresponding linked-list node, allowing O(1) lookup. 
# The doubly linked list maintains the usage order, with the least recently used node near the left side and the most recently used node near the right side. 
#  Whenever I call `get` or update an existing key with `put`, I remove that node from its current position and move it to the most recently used position. 
#  When the cache exceeds its capacity, I remove the node immediately after the left dummy node and delete its key from the HashMap.
#  Because lookup, removal, and insertion are all O(1), both `get` and `put` run in O(1) time.

# ---

# I need both fast lookup by key and fast updates to usage order. A hash map gives me O(1) average-time lookup, but by itself it can’t efficiently tell me which item was least recently used.

# So I combine the hash map with a doubly linked list. The map stores each key to its node, and the linked list keeps nodes ordered from least-recently-used on the left to most-recently-used on the right.

# I use two dummy nodes — left and right — as sentinels. Real nodes always sit between them. The node right after left is the least recently used, and the node right before right is the most recently used. The dummies remove special cases when inserting or removing at the ends.

# The remove helper unlinks a node by connecting its previous and next neighbors directly to each other. The insert helper places a node immediately before the right dummy, marking it most recently used. Both are O(1) because every node already has prev and next pointers.

# In get: if the key is missing I return –1. If it exists I remove its node and re-insert it at the most-recently-used end (because accessing it updates its recency), then return its value.

# In put: if the key already exists I remove the old node. I create a new node with the updated value, insert it at the most-recently-used end, and update the map. If the cache exceeds capacity I remove the node right after the left dummy and delete its key from the map.

# This keeps the list and map in sync, and both get and put run in O(1) average time.
