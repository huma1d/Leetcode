class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        a=0
        x1=x
        while x1>0:
            r=x1%10
            x1//=10
            a+=r
        if x%a==0:
            return a
        return -1
        