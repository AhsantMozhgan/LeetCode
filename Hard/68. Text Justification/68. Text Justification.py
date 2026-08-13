# https://leetcode.com/problems/text-justification

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        result = []
        current_words = []
        current_length = 0

        for word in words:

            # Check if the word fits in the current line.
            if current_length + len(word) + len(current_words) > maxWidth:

                # Number of spaces needed for this line.
                total_spaces = maxWidth - current_length
                number_of_gaps = len(current_words) - 1

                # Single-word line.
                if number_of_gaps == 0:
                    line = current_words[0] + " " * total_spaces

                else:
                    minimum_spaces = total_spaces // number_of_gaps
                    extra_spaces = total_spaces % number_of_gaps

                    line = ""

                    for i, current_word in enumerate(current_words):
                        line += current_word

                        if i < number_of_gaps:
                            spaces = minimum_spaces

                            if i < extra_spaces:
                                spaces += 1

                            line += " " * spaces

                result.append(line)

                # Start a new line.
                current_words = []
                current_length = 0

            current_words.append(word)
            current_length += len(word)

        # Last line: left-justified.
        line = " ".join(current_words)
        result.append(line + " " * (maxWidth - len(line)))

        return result
        

# I’d solve this with a greedy line-building approach.  

# I keep adding words to the current line for as long as the words, plus at least one space between each pair, still fit inside `maxWidth`.  

# When the next word no longer fits, I justify the completed line. I first calculate the total number of spaces needed by subtracting the combined length of the words from `maxWidth`.  

# - If there are multiple words, I distribute those spaces as evenly as possible across the gaps. Any leftover spaces go into the leftmost gaps, one by one.  
# - If the line has only a single word, I left-justify it by putting all the remaining spaces after that word.  

# Then I start a fresh line and continue.  

# Finally I handle the last line separately: I join its words with a single space and pad any remaining spaces on the right, because the last line must be left-justified.  

# Every word is examined only once, so the whole solution is O(n) in the total number of characters and uses O(n) space for the output.
