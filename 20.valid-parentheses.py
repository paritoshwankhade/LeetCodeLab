#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack, lookup = [], {"(":")", "[":"]", "{":"}"}
        for ch in s:
            if ch in lookup:
                stack.append(ch)
            else:
                if len(stack)==0 or lookup[stack.pop()] != ch:
                    return False
        return len(stack)==0
        
# @lc code=end

