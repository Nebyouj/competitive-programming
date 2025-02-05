class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []

        l = 0
        r = len(nums) - 1

        while l <= r:
            if l == r:
                res.append(nums[l])
            else:
                res.append(nums[r])
                res.append(nums[l])
            l += 1
            r -= 1

        return res
