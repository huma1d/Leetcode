class Solution:
    def countDigits(self, num: int) -> int:
        a=0
        num1=num
        while num>0:
            r=num%10
            if num1%r==0:
                a+=1
            num//=10
        return a