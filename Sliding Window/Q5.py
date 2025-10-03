# https://neetcode.io/problems/minimum-window-with-characters

# Minimum Window Substring
# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

# Example 1:

# Input: s = "OUZODYXAZV", t = "XYZ"

# Output: "YXAZ"
# Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

# Example 2:

# Input: s = "xyz", t = "xyz"

# Output: "xyz"
# Example 3:

# Input: s = "x", t = "xy"

# Output: ""
# Constraints:

# 1 <= s.length <= 1000
# 1 <= t.length <= 1000
# s and t consist of uppercase and lowercase English letters.

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        frequency = Counter(t)

        res, resLen = [-1, -1], float("infinity")
        for i in range(len(s)):
            count = {}
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)

                flag = True
                for c in frequency:
                    if frequency[c] > count.get(c, 0):
                        flag = False
                        break

                if flag and (j - i + 1) < resLen:
                    resLen = j - i + 1
                    res = [i, j]

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
