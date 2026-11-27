class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        target = {}
        window = {}
        for ch in t:
            target[ch] = target.get(ch, 0) + 1

        have = 0
        need = len(target)
        res = [-1, -1]
        resLen = float('inf')
        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in target and window[s[r]] == target[s[r]]:
                have+=1
                
            while have == need:
                if r-l+1 < resLen:
                    resLen = r-l+1
                    res = [l, r]

                window[s[l]] -= 1
                if s[l] in target and window[s[l]] < target[s[l]]:
                    have-=1
                l+=1
        l, r = res
        return s[l : r+1] if resLen != float('inf') else ""