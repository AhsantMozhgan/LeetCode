# https://leetcode.com/problems/substring-with-concatenation-of-all-words

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_length = len(words[0])
        number_of_words = len(words)
        total_length = word_length * number_of_words

        required_words = Counter(words)
        result = []

        for offset in range(word_length):
            left = offset
            right = offset
            current_word_count = 0
            current_words = {}

            while right + word_length <= len(s):
                # Extract one complete word
                current_word = s[right:right + word_length]
                right += word_length

                if current_word not in required_words:
                    # Start a completely new window
                    current_words.clear()
                    current_word_count = 0
                    left = right
                    continue

                # Add the extracted word to the current window
                current_words[current_word] = current_words.get(current_word, 0) + 1
                current_word_count += 1

                # While we have too many of the current word, move the left pointer
                while current_words[current_word] > required_words[current_word]:
                    left_word = s[left:left + word_length]
                    current_words[left_word] -= 1
                    current_word_count -= 1
                    left += word_length

                # Found a valid substring
                if current_word_count == number_of_words:
                    result.append(left)

                    # Move the left pointer forward for new checks
                    left_word = s[left:left + word_length]
                    current_words[left_word] -= 1
                    current_word_count -= 1
                    left += word_length

        return result


# I’d use a sliding window together with a frequency map. Because every word has the same length, I scan the string in chunks of `word_length` instead of character by character.  

# First I build a frequency map of the words I need to find. The target substring length is simply the number of words times the length of each word.  

# I then run a separate sliding window for every possible starting offset from 0 to `word_length - 1`. That’s important because valid word boundaries can begin at different character positions. 
# Inside each offset, both pointers jump by one full word at a time.  

# - When I encounter a word that isn’t in the required map, the current window is invalid, so I clear the frequency counts and restart the window after that word.  
# - When the word is required, I add it to the current window. If its count exceeds the needed frequency, I shrink the window from the left one word at a time until the count becomes valid again.  

# Whenever the window contains exactly the right number of words with the correct frequencies, I record the left index as a starting position.
#  Then I remove the leftmost word and advance left so I can keep looking for overlapping matches.  

# This avoids checking every possible substring from scratch. The overall scan is O(n) time, and the extra space is O(k) for the frequency maps, where k is the number of distinct words.”

