class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hash_map = {} #val, indx

       for i , v in enumerate(nums):

        if target-v in hash_map:

            return i,hash_map[target-v]
        else:

            hash_map[v] = i

                
                    
