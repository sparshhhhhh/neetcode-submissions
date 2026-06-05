class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = defaultdict(list)
        for s in strs:
            mpp["".join(sorted(s))].append(s)
        print(mpp)
        res = []
        for i, val in mpp.items():
            res.append(val)
        return res