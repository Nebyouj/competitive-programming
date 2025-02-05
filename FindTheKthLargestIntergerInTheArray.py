class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        numSorted = sorted(map(int, nums), reverse = True)

        return str(numSorted[k - 1])
