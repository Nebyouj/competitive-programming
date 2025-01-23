class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        prefixLenght = len(prefix)

        for s in strs:
            while prefix != s[:prefixLenght]:
                prefixLenght -= 1
                prefix = prefix[:prefixLenght]
            
            if prefixLenght == 0:
                return ""
            

        return prefix
