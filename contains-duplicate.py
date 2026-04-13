class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        w = set(nums)
        if len(w) != len(nums):
            return True
        else:
            return False
