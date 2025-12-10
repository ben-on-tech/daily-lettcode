class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        max_val = max(nums)
        max_target = min(2 * max_val + 1,200005)
        suffix_count = [0]*max_target
        for num in nums:
            if num < max_target:
                suffix_count[num] += 1
        total_triplets = 0
        prefix_count = [0] * max_target
        for j in range(n):
            current_val = nums[j]
            target_val = 2 * current_val
            
            if current_val < max_target:
                suffix_count[current_val] -= 1
            if target_val < max_target:
                count_L = prefix_count[target_val]
                count_R = suffix_count[target_val]
                total_triplets = (total_triplets + count_L * count_R) % MOD
            if current_val < max_target:
                prefix_count[current_val] += 1
        return total_triplets
