class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mpp = {}
        for i in s:
            mpp[i] = mpp.get(i, 0) + 1
        for i in t:
            if i not in mpp.keys():
                return False
            if mpp[i] == 0:
                return False
            mpp[i] -= 1
        return True
