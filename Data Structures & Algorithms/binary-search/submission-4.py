class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums)-1
        while s<=e:
            mid = s + (e-s)//2
            print(s, e, mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                s = mid+1
            else:
                e = mid-1
        return -1