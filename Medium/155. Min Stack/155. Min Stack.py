# https://leetcode.com/problems/min-stack

class MinStack:

    # stack stores all values.
    # min_stack stores the minimum value at each level of the stack.
    def __init__(self):
        self.stack = []
        self.min_stack = []

    # Add a value to the stack.
    def push(self, val: int) -> None:

        # Add the value to the normal stack.
        self.stack.append(val)

        # If min_stack is empty, the current value is the minimum.
        if not self.min_stack:
            self.min_stack.append(val)

        else:
            # The current minimum is at the top of min_stack.
            current_minimum = self.min_stack[-1]

            # The new minimum is the smaller of the new value and the old minimum.
            new_minimum = min(val, current_minimum)

            # Store the new minimum.
            self.min_stack.append(new_minimum)

    # Remove the top value.
    def pop(self) -> None:
        # Remove the top value from both stacks.
        self.stack.pop()
        self.min_stack.pop()

    # Return the top value of the normal stack.
    def top(self) -> int:
        return self.stack[-1]

    # The smallest value is always at the top of min_stack.
    def getMin(self) -> int:
        return self.min_stack[-1]

# Example usage
if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    
    print(min_stack.getMin())  # Output: -3
    min_stack.pop()
    print(min_stack.top())      # Output: 0
    print(min_stack.getMin())   # Output: -2

# I use two stacks. The first stack stores all the values, and the second stack keeps track of the minimum value at each position. When I push a value, I push the smaller of the new value and the current minimum onto the minimum stack. When I pop, I pop from both stacks. This allows `getMin()` to return the top of the minimum stack in O(1).

# ---
# “A normal stack can push, pop, and return its top value in constant time, but finding the minimum would normally require scanning every element.  

# To support getMin() in O(1) time I keep two synchronized stacks.  

# The main stack stores every value exactly as a regular stack would.  
# The second stack — the min stack — stores the minimum value that corresponds to each level of the main stack.

# When I push a value I first push it onto the main stack.  
# Then I look at the current minimum (the top of the min stack) and push the smaller of the two onto the min stack.  
# If the min stack is empty, the new value itself becomes the minimum.

# When I pop I pop from both stacks so they stay aligned.  
# The top of the main stack is the ordinary top value, and the top of the min stack is always the minimum among all values currently present.

# For example, after pushing 5, then 2, then 4:  
# the main stack is [5, 2, 4]  
# the min stack is [5, 2, 2].  

# Even though 4 is on top, the current minimum is still available instantly as 2.”
