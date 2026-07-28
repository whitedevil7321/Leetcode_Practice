from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_index={}
        for i in range(len(nums)):
            left=target-nums[i]
            if left in nums_to_index:
                return [nums_to_index[left],i]
            else:
                nums_to_index[nums[i]]=i
