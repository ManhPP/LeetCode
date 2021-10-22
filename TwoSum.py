class Solution:
    def twoSum(self, nums, target):
        pre_val = {}

        for i, v in enumerate(nums):
            val = target - v
            if val in pre_val:
                return i, pre_val[val]
            pre_val[v] = i