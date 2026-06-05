class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mpp = {}
        for i in nums:
            mpp[i] = mpp.get(i, 0) + 1
        desc_mpp = dict(sorted(mpp.items(), key = lambda item: item[1], reverse = True))
        res = []
        for i in desc_mpp:
            if k == 0:
                return res
            res.append(i)
            k-=1
        return res