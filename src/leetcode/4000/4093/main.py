class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        increases = []
        for i in range(len(nums)):
            n = nums[i]
            n_max = int(''.join(sorted(str(n), reverse=True)))
            increases.append(n_max - n)
        increases = sorted(increases, reverse=True)
        ans = sum(nums)
        for i in range(len(increases)):
            if i >= k:
                break
            elif increases[i] > 0:
                ans += increases[i]
            else:
                break
        return ans
