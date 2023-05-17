#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
#idea: sort the intervals by their start value, then we can merge all the intervals in one pass
#because the intervals are sorted by start value, we only need to compare the end value of the previous interval with the start value of the current interval
#time complexity: O(nlogn) because of sorting
#space complexity: O(1) if we can sort intervals in place, O(n) otherwise

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        merged = []
        for interval in sorted_intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max()
# @lc code=end

