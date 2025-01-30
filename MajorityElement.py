class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = Counter(nums)
        n = len(nums)

        for num, count in majority.items():
            if count > (n//2):
                return num
