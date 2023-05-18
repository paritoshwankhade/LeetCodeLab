#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        loc_length = 0
        max_len = 0
        start = 0
        
        for i in range(len(s)):
            if s[i] in hash and hash[s[i]] >= start:
                start = hash[s[i]] + 1
            else:
                loc_length = i - start + 1
                max_len = max(max_len, loc_length)
            
            hash[s[i]] = i
        
        return max_len


# @lc code=end

