class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert integer to string for easy comparison of digits
        str_x = str(x)

        # Compare characters from left to right and right to left
        return str_x == str_x[::-1]


# Example usage:
solution = Solution()

# Example 1
x1 = 121
output1 = solution.isPalindrome(x1)
print(output1)  # Output: True

# Example 2
x2 = -121
output2 = solution.isPalindrome(x2)
print(output2)  # Output: False

# Example 3
x3 = 10
output3 = solution.isPalindrome(x3)
print(output3)  # Output: False
