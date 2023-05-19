#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ind1 = -1
        for i, num in enumerate(nums):
            if num == 0:
                if ind1>=0:
                    return [0] * len(nums)
                else:
                    ind1 = i
        if ind1>=0:
            product = 1
            for i, num in enumerate(nums):
                if i != ind1:
                    product *= num
            return [0] *ind1 + [product] + [0] * (len(nums)-ind1-1)
        else:
            product = 1
            for num in nums:
                product *= num
            return [product//num for num in nums]
                                
# @lc code=end