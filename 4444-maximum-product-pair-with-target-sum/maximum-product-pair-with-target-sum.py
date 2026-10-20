class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        x = 0
        y = 0
        z = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    if nums[i] > nums[j]:
                        if x == 0 and y == 0:
                            x = i
                            y = j
                        else:
                            if nums[i] * nums[j] >= nums[x] * nums[y]:
                                x = i
                                y = j
        if x == 0 and y == 0:
            z.append(-1)
            z.append(-1)
        else:
            z.append(x)
            z.append(y)
        return z
        
        