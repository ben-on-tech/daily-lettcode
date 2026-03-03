class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        result = []  # This will store all unique combinations that sum up to the target.
        
        def backtrack(start: int, target: int, current: List[int]):
            # Base case: If the target is exactly 0, it means the current combination adds up to the target.
            if target == 0:
                result.append(list(current))  # Add a copy of the current combination to the result list.
                return  # Return to explore other potential combinations.
            
            
            for i in range(start, len(candidates)):
                
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                
                
                if candidates[i] > target:
                    break
                
                
                current.append(candidates[i])
                
                
                backtrack(i + 1, target - candidates[i], current)
                
                
                current.pop()
        
        
        backtrack(0, target, [])
        
       
        return result
