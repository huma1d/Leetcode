class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        else:
            a=[0]*len(nums)
            a[0]=nums[0]
            a[1]=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                a[i]=max(a[i-1],nums[i]+a[i-2])
            b=a[len(a)-1]
            return b    