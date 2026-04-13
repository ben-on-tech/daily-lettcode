class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d={}
        for i, num in enumerate(sorted(nums)):
            if num not in d:
                d[num] = i

        ret = []

        for i in nums:
            ret.append(d[i])
        return ret
                
