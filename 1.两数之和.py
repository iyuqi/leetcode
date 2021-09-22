#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
# 解法一：常规嵌套循环查找，时间复杂度O(n^2)

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length=len(nums)
        for i in range(0, length):
            for j in range(i+1, length):
                if(nums[i] + nums[j] ==  target):
                    return [i,j]
        return None
# @lc code=end