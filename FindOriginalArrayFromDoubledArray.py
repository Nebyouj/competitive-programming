class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        res = []

        if len(changed) % 2 != 0:
            return []

        count = Counter(changed)

        for num in sorted(count.keys()):
            if num == 0:
                if count[num] % 2 != 0:
                    return []
                res.extend([0] * (count[num] // 2))
            else:
                if count[num] > count[num * 2]:
                    return []
                res.extend([num] * count[num])
                count[num * 2] -= count[num]

        return res












        # res = []
        # if len(changed) % 2 != 0:
        #     return res

        # if len(changed) == 2 and changed[0] == changed[1] * 2:
        #     res.append(changed[1])
        #     return res

        # n = len(changed)//2
        # for i in range(n):
        #     if changed[i] * 2 != changed[n + i]:
        #         return []
        #     else:
        #         res.append(changed[i])

        # return res
