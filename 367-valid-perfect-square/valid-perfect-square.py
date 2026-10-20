class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=0
        r=num
        while r>=l:
            mid=l+(r-l)//2
            if mid*mid==num:
                return True
            elif mid*mid>num:
                r=mid-1
            else:
                l=mid+1
        return False
        # l = 0
        # r = num
        # while l <= r:
        #     z = l + (r-l) // 2
        #     if z * z == num:
        #         return True
        #     elif z * z < num:
        #         l = z + 1
        #     else:
        #         r = z - 1
        # return False