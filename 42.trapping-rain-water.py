#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
#idea 1: brute force
# for each element, find the max height on the left and right
# the water it can trap is min(left_max, right_max) - height[i]
# time complexity: O(n^2)
# space complexity: O(1)
# idea 2: dynamic programming
# for each element, find the max height on the left and right
# the water it can trap is min(left_max, right_max) - height[i]
# finding min(left_max, right_max) in O(n) time explaination:
# we can use two arrays to store the left_max and right_max for each element

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        left_max[0] = height[0]
        right_max[-1] = height[-1]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i])
        for i in range(len(height)-2, 0, -1):
            right_max[i] = max(right_max[i+1], height[i])
        water = 0
        for i in range(1, len(height)-1):
            water += min(left_max[i], right_max[i]) - height[i]
        return water

# @lc code=end