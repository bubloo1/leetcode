from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            if length + len(line) + len(words[i]) > maxWidth:
                extraSpace = maxWidth - length
                spaces = extraSpace // max(1, len(line) - 1)
                remainder = extraSpace % max(1, len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spaces
                    if remainder:
                        line[j] += " "
                        remainder -= 1
                
                res.append("".join(line))
                line, length = [],0
            
            line.append(words[i])
            length += len(words[i])
            i += 1

        lastLine = " ".join(line)
        trailSpace = maxWidth - len(lastLine)
        res.append(lastLine + " " * trailSpace)
        return res



newObject = Solution()
print(newObject.fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16))