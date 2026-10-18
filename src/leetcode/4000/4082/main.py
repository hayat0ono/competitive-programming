class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        now = nums[0]
        ans = 0
        for i in range(1, len(nums)):
            if now != nums[i]:
                now = nums[i]
            else:
                ans += 1
        return ans
    