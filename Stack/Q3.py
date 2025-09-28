# https://neetcode.io/problems/evaluate-reverse-polish-notation

# Evaluate Reverse Polish Notation
# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

# Return the integer that represents the evaluation of the expression.

# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.
# Example 1:

# Input: tokens = ["1","2","+","3","*","4","-"]

# Output: 5

# Explanation: ((1 + 2) * 3) - 4 = 5
# Constraints:

# 1 <= tokens.length <= 1000.
# tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1: return tokens.pop()
        if len(tokens) < 3: return 0
        for token in tokens:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                if stack == []: return 0
                else:
                    num1, num2 = stack.pop(), stack.pop()
                    if token == '+':
                        stack.append(num2+num1)
                    elif token == '-':
                        stack.append(num2-num1)
                    elif token == '*':
                        stack.append(num2*num1)
                    elif token == '/':
                        stack.append(int(num2/num1))
        if stack == []:
            return 0
        return stack.pop()
