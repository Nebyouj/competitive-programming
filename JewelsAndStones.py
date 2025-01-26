class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stoneToNumber = {}

        for stone in stones:
            stoneToNumber[stone] = 1 + stoneToNumber.get(stone, 0)

        output = 0
        for jewel in jewels:
            if jewel in stoneToNumber:
                output += stoneToNumber[jewel]

        return output
