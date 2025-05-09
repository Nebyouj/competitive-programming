class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l , r = 0, len(nums) - 1
        i = 0

        def swap(i,p):
            tmp = nums[i]
            nums[i] = nums[p]
            nums[p] = tmp

        while i <= r:
            if nums[i] == 0:
                swap(i,l)
                l += 1
            if nums[i] == 2:
                swap(i,r)
                r -= 1
                i -= 1
            i += 1
