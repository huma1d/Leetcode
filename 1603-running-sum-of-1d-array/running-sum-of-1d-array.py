class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        a=[]
        a.append(nums[0])
        for i in range(1,len(nums)):
            a.append(a[i-1]+nums[i])
        return a

        