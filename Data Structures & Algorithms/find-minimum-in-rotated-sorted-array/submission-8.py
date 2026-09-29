class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[len(nums) - 1]:
            return nums[0]
        
        l, r = 0, len(nums) - 1

        while l <= r:
            if l + 1 == r:
                return min(nums[l], nums[r])
            mid = l + int((r - l) / 2)
            # print(l,mid,r)
            if nums[mid] < nums[(mid + len(nums) - 1) % len(nums)]:
                return nums[mid]

            if nums[l] > nums[mid]:
                r = mid
            else:
                l = mid

