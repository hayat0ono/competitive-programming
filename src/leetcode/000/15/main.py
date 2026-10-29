class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        sorted_unique_nums = sorted(nums_dict.keys())
        for x in sorted_unique_nums:
            if nums_dict[x] >= 3 and x == 0:
                ans.append([x, x, x])
            if nums_dict[x] >= 2 and (-2) * x in nums_dict and x != 0:
                ans.append([x, x, (-2) * x])
            for y in sorted_unique_nums:
                if x >= y:
                    continue
                z = - x - y
                if z > y and z in nums_dict:
                    ans.append([x, y, z])
        return ans
