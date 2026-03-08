class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        a = [int(ch) for ch in s]

        
        m0 = 0
        for i, bit in enumerate(a):
            expected = i % 2          
            if bit != expected:
                m0 += 1

        
        if n % 2 == 0:
            return min(m0, n - m0)

        
        ans = min(m0, n - m0)
        cur = m0
        for k in range(n - 1):
            
            cur = n - 1 - cur + 2 * a[k]
            ans = min(ans, min(cur, n - cur))
        return ans
