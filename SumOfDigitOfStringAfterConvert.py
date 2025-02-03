class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = []
        for i in range(len(s)):
            res.append((ord(s[i]) - ord('a')) + 1)
        a = ''
        a = ''.join(map(str,res))
        inta = int(a)

        def sumOf(a):
            output = 0
            while a:
                digit = a % 10
                output += digit
                a //= 10
            return output

        while k > 0:
            inta = sumOf(inta)
            k -= 1

        return inta
            

        


      

        



        
