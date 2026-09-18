class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_seen = {}
        for ind, num in enumerate(nums):
            if target - num in nums_seen:
                return [nums_seen.get(target - num), ind]
            else:
                nums_seen[num] = ind