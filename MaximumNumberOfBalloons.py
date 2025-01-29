from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter("balloon")
        textMap = Counter(text)

        m = float('inf')
        for char, count in balloon.items():
            m = min(m,textMap[char]//count)

        return m


        
        # textMap ={}
        # count = []

        # for t in text:
        #     if t in "balloon":
        #         count.append(t)

        # for t in count:
        #     textMap[t] = 1 + textMap.get(t,0)
        
        # m = float('inf')
        # for val in textMap.values():
        #     if len(textMap) < 5 or textMap["l"] < 2 or textMap["o"] < 2:
        #         return 0
        #     m = min(val,m)

        # return m if m != float('inf') else 0
        
