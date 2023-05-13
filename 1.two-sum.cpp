/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    std::unordered_map<int, int> numMap;
    std::vector<int> result;

    for (int i = 0; i < nums.size(); ++i) {
        int complement = target - nums[i];
        if (numMap.count(complement)) {
            result.push_back(numMap[complement]);
            result.push_back(i);
            break;
        }
        numMap[nums[i]] = i;
    }

    return result;
    }
};
// @lc code=end

