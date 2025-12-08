class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c_squared = a * a + b * b
                
                for c in range(1, n + 1):
                    c_current_squared = c * c
                    
                    if c_current_squared == c_squared:
                        count += 1
                        break
                    
                    if c_current_squared > c_squared:
                        break
                        
        return count
