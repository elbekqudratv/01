from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""  # If the input list is empty, return an empty string

        # Iterate through characters of the first string
        for i, char in enumerate(strs[0]):
            # Check if the character is common to all strings
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return strs[0][:i]  # Return the common prefix up to the current character

        return strs[0]  # If loop completes, the first string is the common prefix


# Example usage:
solution = Solution()

# Example 1
strs1 = ["flower", "flow", "flight"]
output1 = solution.longestCommonPrefix(strs1)
print(output1)  # Output: "fl"

# Example 2
strs2 = ["dog", "racecar", "car"]
output2 = solution.longestCommonPrefix(strs2)
print(output2)  # Output: ""
