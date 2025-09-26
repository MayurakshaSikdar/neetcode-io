# https://neetcode.io/problems/string-encode-and-decode

# Encode and Decode Strings
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]
# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for str in strs:
            encoded_str += f'{len(str)}#{str}'
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i, j, n = 0, 0, len(s)
        result = []
        while j<n:
            if s[j] == '#':
                try:
                    char_count = int(s[i:j])
                    word = s[j+1: j+char_count+1]
                    result.append(word)
                    i = j+char_count+1
                    j = j+char_count+1
                except:
                    raise Exception()
            else:
                j += 1
        return result
