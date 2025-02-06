class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        if len(ranges) == 1:
            if ranges[0][0] <= left and ranges[0][1] >= right:return True
            else: return False

        ranges.sort()
        for start, end in ranges:
            if end < left: continue
            if start > left: return False
            if end >= right: return True
            left = end + 1
        return False
