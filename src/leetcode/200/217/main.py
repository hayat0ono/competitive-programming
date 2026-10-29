class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                return True
            else:
                nums_dict[num] = 1
        return False
