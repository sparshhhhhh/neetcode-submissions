class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m > n:
            return False
        target = [0]*26
        window = [0]*26
        base = ord('a')
        for i in range(m):
            target[ord(s1[i]) - base] += 1
            window[ord(s2[i]) - base] += 1

        if window == target:
            return True
        
        for r in range(m, n):
            window[ord(s2[r]) - base] += 1
            window[ord(s2[r-m]) - base] -= 1
            if window == target:
                return True
            
        return False
                