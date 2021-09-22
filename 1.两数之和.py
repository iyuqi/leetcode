#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
# 解法一：采用嵌套循环解问题1，时间复杂度O(n^2)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         length=len(nums)
#         for i in range(0, length):
#             for j in range(i+1, length):
#                 if(nums[i] + nums[j] ==  target):
#                     return [i,j]
#         return None
#
# 解法二：利用字典模拟哈希表解问题1，时间复杂度O(n)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap={}
#         for index, num in enumerate(nums):
#             hashmap[num] = index
#         for i, num in enumerate(nums):
#             j = hashmap.get(target-num)
#             if j is not None and i!=j:
#                 return [i,j]
#         return None
#
# 解法三：省略初始化字典优化时间
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap={}
#         for i, num in enumerate(nums):
#             if hashmap.get(target - num) is not None:
#                 return [hashmap.get(target - num), i]
#             hashmap[num] = i
#         return None
#
# 解法四：优化解法一
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             if target-nums[i] in nums[i+1:]:
#                 return [i, nums[i+1:].index(target-nums[i])+i+1]


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]:
                return [i, nums[i+1:].index(target-nums[i])+i+1]
# @lc code=end