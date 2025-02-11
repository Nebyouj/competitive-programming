class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        return ''.join(char*freq for char,freq in freq.most_common())
