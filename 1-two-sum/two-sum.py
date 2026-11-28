class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        c=nums.copy()
        c.sort()
        left=0
        right=len(c)-1
        x=-1
        y=-1
        while right>left:
            if c[left]+c[right]==target:
                break
            elif c[left]+c[right]>target:
                right-=1
            elif c[left]+c[right]<target:
                left+=1
        for i in range(len(nums)):
            if x<0:
                if nums[i]==c[left]:
                    x=i
            if nums[i]==c[right]:
                y=i
        b = [x,y]
        return b