class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        pillowPosition = 1
        currentTime = 0
        direction = 1
        while currentTime < time:
            if n >= pillowPosition + direction > 0:
                pillowPosition += direction
                currentTime += 1
            else:
                direction *= -1

        return pillowPosition 
