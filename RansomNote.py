class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = {}
        mag = {}

        for r in ransomNote:
            ransom[r] = 1 + ransom.get(r, 0)
        for m in magazine:
            mag[m] = 1 + mag.get(m, 0)

        for char,count in ransom.items():
            if mag.get(char, 0) < count:
                return False

        return True
