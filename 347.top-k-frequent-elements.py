#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        for num in nums:
            mydict[num] = mydict.get(num, 0) +1
        sorted_dict = sorted(mydict.items(), key=lambda x:x[1], reverse=True)
        temp = 0
        ans = []
        for num in sorted_dict:
            temp+=1
            ans.append(num[0])
            if temp==k:
                return ans
# @lc code=end

