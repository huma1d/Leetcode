class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n>=10 and n<=18:
            return True
        elif n>26 and n<=33:
            return True
        elif n>39 and n<=44:
            return True
        elif n>48 and n<=50:
            return True
        return False
        