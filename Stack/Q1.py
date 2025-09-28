# https://neetcode.io/problems/validate-parentheses

# Valid Parentheses
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Example 1:

# Input: s = "[]"

# Output: true
# Example 2:

# Input: s = "([{}])"

# Output: true
# Example 3:

# Input: s = "[(])"

# Output: false
# Explanation: The brackets are not closed in the correct order.

# Constraints:

# 1 <= s.length <= 1000

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        stack = []
        for i in s:
            if i in ('(', '{', '['):
                stack.append(i)
            elif stack == []: return False
            else:
                if stack[-1] == '(' and i != ')': return False
                elif stack[-1] == '{' and i != '}': return False
                elif stack[-1] == '[' and i != ']': return False
                else: stack.pop()
        if stack == []:
            return True
        return False
