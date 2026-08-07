# https://leetcode.com/problems/insert-delete-getrandom-o1

class RandomizedSet:
    def __init__(self):
        self.data = []  # List to store elements
        self.index_map = {}  # Map to store index of elements

    def insert(self, val: int) -> bool:
        if val in self.index_map:  # Check if the value already exists
            return False  # Value already present
        self.index_map[val] = len(self.data)  # Map the value to its index
        self.data.append(val)  # Append the value to the list
        return True  # Successful insertion

    def remove(self, val: int) -> bool:
        if val not in self.index_map:  # Check if the value exists
            return False  # Value not found
        # Get the index of the element to be removed
        index = self.index_map[val]
        last_element = self.data[-1]  # Get the last element

        # Move the last element to the position of the element to remove
        self.data[index] = last_element
        self.index_map[last_element] = index  # Update the index of the last element

        # Remove the last element
        self.data.pop()  # This operation decreases the size of the list

        # Remove from index_map
        del self.index_map[val]

        return True  # Successful removal

    def getRandom(self) -> int:
        return random.choice(self.data)  # Return a random element from the list
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# To support insert, remove, and getRandom in average O(1) time, I combine a list and a hash map.  

# The list holds all the values so I can pick a random element just by choosing a random index.  
# The hash map stores each value’s current index in the list, which lets me check existence and locate an element instantly for removal.  

# For insertion I first check whether the value is already in the map. If it isn’t, I append it to the list and record its index.  

# For removal I can’t delete from the middle of the list without shifting elements. Instead I swap the target with the last element in the list, 
# update the moved element’s index in the map, pop the last element, and delete the target from the map.  

# getRandom simply calls `random.choice` on the list, so every value has an equal chance of being returned.  

# All three operations run in average O(1) time, and the whole structure uses O(n) space.
