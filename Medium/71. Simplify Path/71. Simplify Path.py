# https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path: str) -> str:

        # The stack stores the directories that are currently part of the path.
        stack = []

        # Split the path using "/".
        parts = path.split("/")

        # Process Each Part
        for current_part in parts:


            # Empty Part or "." .
            # An empty part usually comes from consecutive slashes. The empty part has no meaning.
            # "." also means the current directory, so it changes nothing.
            if current_part == "" or current_part == ".":
                continue

            # ".." means: Go to the parent directory.
            # If the stack is not empty, remove the last directory.
            elif current_part == "..":

                if stack:
                    stack.pop()

            # Normal Directory
            # If it is a normal directory, add it to the stack.
            else:
                stack.append(current_part)

        # Build the Final Path
        # Join all remaining directories with "/".
        return "/" + "/".join(stack)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.simplifyPath("/a/./b/../../c/"))  # Output: "/c"
    print(solution.simplifyPath("/../"))              # Output: "/"
    print(solution.simplifyPath("/home//foo/"))       # Output: "/home/foo"
    print(solution.simplifyPath("/a/../../b/../c/"))  # Output: "/c"
    print(solution.simplifyPath("/.../"))             # Output: "/..."

# I use a stack to keep track of the directories in the current path. I split the path by `/` and process each component. 
# Empty components and `"."` can be ignored. For `".."`, I pop the most recent directory from the stack if one exists. 
# For normal directory names, I push them onto the stack. Finally, I join the remaining directories with `/` and add the leading slash.

# ---

# I need to convert an absolute Unix-style path into its canonical form. I use a stack to keep track of the directories that will remain in the final path.

# First I split the input on every `/`. That produces the individual path components plus some empty strings from consecutive slashes.

# Then I process each component:

# - Empty strings and `.` are ignored — they don’t change the current location.  
# - `..` means go up one level, so I pop the top directory from the stack if it isn’t empty. If the stack is already empty I simply stay at the root.  
# - Anything else is a real directory name, so I push it onto the stack.

# Finally I join whatever is left on the stack with `/` and put a single leading slash in front.  
# If the stack is empty the result is just `/`, which is correct.