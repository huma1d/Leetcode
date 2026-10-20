class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        c=0
        x=0
        for i in range(len(gain)):
            x=x+gain[i]
            if x>c:
                c=x
        return c


        