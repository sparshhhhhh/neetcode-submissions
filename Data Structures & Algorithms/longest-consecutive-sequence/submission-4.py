class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        mpp = {}
        mpp[nums[0]] = True
        maxSub = 1
        l = 1
        for i in range(1, len(nums)):
            if nums[i] not in mpp:
                mpp[nums[i]] = True
                if (nums[i] - 1) in mpp:
                    l+=1
                    maxSub = max(maxSub, l)
                else:
                    maxSub = max(maxSub, l)
                    l = 1
        return maxSub