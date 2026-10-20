class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        b = []
        x = -1
        b.append(0)
        b.append(nums[0])
        for i in range(2,len(nums)+1):
            b.append(b[i-1]+nums[i-1])
        n = len(b)
        for j in range(n-1):
            if b[j] == b[n-1]-b[j+1]:
                x = j
                break
        if x > -1:
            return x
        else:
            return -1