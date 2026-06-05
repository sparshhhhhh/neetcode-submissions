class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            j = len(nums)-1
            while i<j:
                if target - nums[i] == nums[j]:
                    return [i, j]
                else:
                    j-=1