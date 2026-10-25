class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        ans = 0
        for start in range(len(nums)):
            rank = {}
            freq = {}
            required_len = 0
            for goal in range(start, len(nums)):
                x = nums[goal]
                if x not in rank:
                    rank[x] = len(rank) + 1
                    freq[x] = 0
                    required_len += rank[x]
                    if required_len > len(nums):
                        break
                freq[x] += 1
                if freq[x] > rank[x]:
                    break
                if goal - start + 1 == required_len:
                    ans += 1
        return ans
